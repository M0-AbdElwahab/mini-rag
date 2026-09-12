try:
    from fastapi import FastAPI  # type: ignore[import-not-found]
except ModuleNotFoundError:
    class FastAPI:
        def get(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator

app = FastAPI()

@app.get("/welcome")
def welcome():
    return {
        "message": "Hello World!"
    }