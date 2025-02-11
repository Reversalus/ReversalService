import aioredis

class RedisHandler:
    def __init__(self, REDIS_URL: str):
        self.redis = aioredis.from_url(REDIS_URL, decode_responses=True)

    async def store_otp(self, phone:str, otp:str, expiry:int=300) -> None:
        await self.redis.setex(f"otp:{phone}", expiry, otp)

    async def verify_otp(self, phone:str, otp:str) -> bool:
        return await self.redis.get(f"otp:{phone}") == otp

    async def delete(self, phone:str) -> None:
        await self.redis.delete(f"otp:{phone}")
