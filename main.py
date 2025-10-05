from fastapi import FastAPI
from blog.routes import app_routes, authentication_router, blog_router, user_router
from blog.models import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/welcome")
def index():
    return {"message": "Hello Shreyansh!, Welcome to the FastAPI application!"}

app.include_router(app_routes.router)
app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(authentication_router.router)