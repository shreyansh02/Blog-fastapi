from typing import Optional
from fastapi import APIRouter, status, Response
from ..controllers import blog_controller
# from ..models.schemas import Blog

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "message": "Health Check OK", 
        "status": "success"
    }

@router.get("/blog/unpublished")
def unpublished_blogs():
    return {
        "data": "List of unpublished blogs"
    }

@router.get("/blog/{id}")
def about_blog(id: int):
    return {
        "data": id
    }

# /v1/blogs?limit=10&published=true
@router.get("/blog")
def get_blogs(
    limit: int = 10, 
    published: bool = True,
    sort: Optional[str] = None
):
    return {
        "data": f"List of all blogs with limit {limit} and published {published}"
    }

# @router.post("/blog/create")
# def create_blog(request: Blog):
#     return {
#         "data": f"Blog is created with title as {request.title}"
#     }
