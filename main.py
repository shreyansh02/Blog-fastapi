from fastapi import FastAPI
from blog.routes import app_routes

app = FastAPI()

@app.get("/welcome")
def index():
    return {"message": "Hello Shreyansh!, Welcome to the FastAPI application!"}

app.include_router(app_routes.router)