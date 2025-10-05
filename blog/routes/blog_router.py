from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import models, schemas
from database import get_db

router = APIRouter(
    prefix="/v1/blog",
    tags=['Blogs']
)

@router.get("/")
def list_blogs(
    db: Session = Depends(get_db)
):
    blogs = db.query(models.Blog).all()
    return blogs
    

@router.post("/")
def create(
    request: schemas.Blog,
    db: Session = Depends(get_db)
):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog