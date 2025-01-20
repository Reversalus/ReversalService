from fastapi import FastAPI, Request, Depends
import httpx

from middleware.validation_middleware import validate_header_source

app = FastAPI(title="API Gateway")

Services = {
    'auth': "http://127.0.0.1:8001",
    'user': "http://127.0.0.1:8002",
}


async def proxy_request(service: str, path: str, method: str, body = None, headers: dict = None):
    async with httpx.AsyncClient() as client:
        response = await client.request(method=method,url= f"{Services[service]}{path}",json=body, headers=headers)
        return response.json()


@app.get("/{service}/{path:path}", dependencies=[Depends(validate_header_source)])
async def gateway_get(service: str, path: str, request: Request):
    headers = dict(request.headers)
    return await proxy_request(service, f"/{path}", "GET", headers=headers)

@app.post("/{service}/{path:path}", dependencies=[Depends(validate_header_source)])
async def gateway_get(service: str, path: str, request: Request, body: dict):
    headers = dict(request.headers)
    return await proxy_request(service, f"/{path}", "POST",body=body, headers=headers)

@app.put("/{service}/{path:path}", dependencies=[Depends(validate_header_source)])
async def gateway_put(service: str, path: str, request: Request, body: dict):
    headers = dict(request.headers)
    return await proxy_request(service, f"/{path}", "PUT", body=body, headers=headers)

@app.delete("/{service}/{path:path}", dependencies=[Depends(validate_header_source)])
async def gateway_delete(service: str, path: str, request: Request):
    headers = dict(request.headers)
    return await proxy_request(service, f"/{path}", "DELETE", headers=headers)  
