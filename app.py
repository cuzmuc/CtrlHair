import json
import requests
import threading
from datetime import datetime
from flask import Flask, request, Response, jsonify, make_response, redirect, render_template

from PIL import Image
from backend import Backend
import cv2
from util.imutil import read_rgb, write_rgb
import io
import numpy as np
from base64 import b64encode, b64decode


IMAGE_PROCESS_OK = 100
IMAGE_PROCESS_ERR = 101
INVALID_REQUEST_ERR = 231
INVALID_IMAGE_ERR = 232
UNKNOWN_ERR = 500

be = Backend(2.5)

input_image = read_rgb('imgs/input_img.png')
target_image = read_rgb('imgs/out_img.png')

"""
If the image need crop
"""
# input_image = be.crop_face(input_image)
# target_image = be.crop_face(target_image)

start_time = datetime.now()

input_image = cv2.resize(input_image, (256, 256))

be.set_input_img(input_image)
be.set_target_img(target_image)

# transfer all latent code from target image to input image
be.transfer_latent_representation('color')
be.transfer_latent_representation('texture')
be.transfer_latent_representation('shape')

# change the variance manually
#be.change_color(1.0, 2)

out_mask = be.get_mask(input_image)
output_img = be.output()
write_rgb('temp.png', output_img)
print(f'Image process takes {datetime.now() - start_time}')

app = Flask(__name__)

def getimage(raw_image):    
    decoded_string = io.BytesIO(b64decode(raw_image))
    img = Image.open(decoded_string).convert('RGB')
    return np.array(img)

@app.route("/")
def hello_world():
    return "<p>Hello, HairSwap API!</p>"
    
@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swapapi.html')

@app.route('/swaphair', methods=['POST'])
def swaphair():
     # POST
    # Read image data
    img_data = request.json
    if 'srcimg' not in img_data or 'dstimg' not in img_data:
        response = {
            'error': INVALID_REQUEST_ERR
        }
        return make_response(jsonify(response), 400)
    
    input_image = getimage(img_data['srcimg'])    
    target_image = getimage(img_data['dstimg'])

    """
    If the image need crop
    """
    # input_image = be.crop_face(input_image)
    # target_image = be.crop_face(target_image)

    be.set_input_img(input_image)
    be.set_target_img(target_image)

    # transfer all latent code from target image to input image
    be.transfer_latent_representation('color')
    be.transfer_latent_representation('texture')
    be.transfer_latent_representation('shape')
   
    output_img = be.output()

    if len(output_img.shape) == 2:
        output_img = np.stack([output_img] * 3, axis=2)
    elif output_img.shape[2] == 1:
        output_img = np.tile(output_img, [1, 1, 3])

    resbgr = cv2.cvtColor(output_img, cv2.COLOR_RGB2BGR)

    _, buffer = cv2.imencode(".png", resbgr)
    imgstr = b64encode(buffer).decode('utf-8')

    response = {
        'resimg': imgstr
    }

    return make_response(jsonify(response), 200)

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0',port=5555,debug=False)