from fastapi import Request, HTTPException

async def validate_header_source(request: Request, call_next):
    source = request.headers.get("source")
    if not source or source not in ['reversal-web', 'reversal-and', 'reversal-ios']:
        raise HTTPException(status_code=403, detail="Invalid or Missing source header")