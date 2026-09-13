try:
    from fastapi import FastAPI  # type: ignore[import-not-found]
except ModuleNotFoundError:
    class FastAPI:
        def get(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator

from routes import base, data


app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)
