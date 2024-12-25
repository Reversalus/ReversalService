from fastapi import FastAPI
from datetime import datetime

from routes.login import loginRouter

app = FastAPI()
start_time = datetime.now()

PORT = 8000

@app.get("/")
def read_root():
    return {"Welcome to the login service"}

@   app.get('/ping')
def ping():
    return {
            "status": "ok",
            "uptime": str(datetime.now() - start_time),
            "port": PORT 
        }

app.include_router(loginRouter)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)