try:
    from fastapi import FastAPI  # type: ignore[import-not-found]
except ModuleNotFoundError:
    class FastAPI:
        def get(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator


from routes import base, data


try:
    from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore[import-not-found]
except ModuleNotFoundError:
    class AsyncIOMotorClient:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError("motor is required to use MongoDB support")

        
from helpers.config import get_settings

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()
    # Initialize MongoDB client
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URI)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()  

app.include_router(base.base_router)
app.include_router(data.data_router)
