from fastapi import FastAPI, Depends
from datetime import datetime

from .routes.auth import router as auth_router

app = FastAPI()

start_time = datetime.now()
PORT = 8000

# ping returns the status of the service
@app.get('/ping')
def ping():
    return {
            "status": "ok",
            "uptime": str(datetime.now() - start_time),
            "port": PORT 
        }

app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)