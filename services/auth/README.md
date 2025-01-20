# Auth Micro Service
This is the micro backend for all services related to user login and onboarding.

To run this app via uvicorn, follow the below instructions.

```sh
cd <path to main.py>
uvicorn services.onboarding.app.main:app --reload --port 8000
```