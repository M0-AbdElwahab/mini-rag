try:
    from fastapi import FastAPI  # type: ignore[import-not-found]
except ModuleNotFoundError:
    class FastAPI:
        def get(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator
        
from dotenv import load_dotenv

load_dotenv(".env")  # Load environment variables from .env file

from src.routes import base


app = FastAPI()

app.include_router(base.base_router)
