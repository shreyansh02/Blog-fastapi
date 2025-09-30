from typing import Optional
from fastapi import APIRouter, status, Response
from ..controllers import app_controller
from ..models.general_models import Blog

router = APIRouter()

@router.get("/v1/health")
def health_check():
    return {
        "message": "Health Check OK", 
        "status": "success"
    }

@router.get("/v1/blog/unpublished")
def unpublished_blogs():
    return {
        "data": "List of unpublished blogs"
    }

@router.get("/v1/blog/{blog_id}")
def about_blog(blog_id: int):
    return {
        "data": blog_id
    }

# /v1/blogs?limit=10&published=true
@router.get("/v1/blogs")
def get_blogs(
    limit: int = 10, 
    published: bool = True,
    sort: Optional[str] = None
):
    return {
        "data": f"List of all blogs with limit {limit} and published {published}"
    }

@router.post("/v1/blog/create")
def create_blog(request: Blog):
    return {
        "data": f"Blog is created with title as {request.title}"
    }
