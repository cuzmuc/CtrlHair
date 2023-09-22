# CtrlHair
Controllable Hair Editing (ECCV 2022)

# Install
Need python3.8 and GPU runtime environment

Clone this repo 

- git clone https://github.com/cuzmuc/CtrlHair.git
- cd CtrlHair

Install python packages

- bash script/install.sh

Download pretrained model and parameters

- python script/download.py

# Run API server

- python app.py

can see PORT and IP here -> (https://github.com/cuzmuc/CtrlHair/blob/b19ec1c7bcb2b8815885cc14bee7588b9ee02c4c/app.py#L117)

# Test API server

- python test.py

  or

  ```
    curl --location --request POST 'http://0.0.0.0:5555/swaphair' \
    --header 'Content-Type: application/json' \
    --data-raw '{ \
      "srcimg": "data:image/png;base64,/9j/4AAQSkZJRgABAQEAYABgAAD....", \
      "dstimg": "data:image/png;base64,/9j/4AAQSkZJRgABAQEAYABgAAD....", \
    }
  ```
  
