# Auth Micro Service
This is the micro backend for all services related to user login and onboarding.

To run this app via uvicorn, follow the below instructions.

```sh
cd <path to main.py>
uvicorn services.onboarding.app.main:app --reload --port 8000
```

> running from docker
```sh 
    # build your image
    docker build -t <image-name> .

    # run you image in a container
    

```