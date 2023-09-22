import base64
import json
import requests

srcimg = ""
dstimg = ""

with open("./imgs/input_img.png", 'rb') as image_file:
    srcimg = base64.b64encode(image_file.read()).decode('UTF-8')
    
with open("./imgs/out_img.png", 'rb') as image_file:
    dstimg = base64.b64encode(image_file.read()).decode('UTF-8')

data = {
    'srcimg':srcimg,
    'dstimg':dstimg,
}
json_data = json.dumps(data)

headers = {
    'Content-type':'application/json', 
    'Accept':'application/json'
}

response = requests.post(url='http://0.0.0.0:5555/swaphair', headers=headers, data=json_data)
return_data = json.loads(response.text)

decodeit = open('result.png', 'wb')
decodeit.write(base64.b64decode(return_data['resimg']))
decodeit.close()


