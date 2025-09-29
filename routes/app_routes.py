from fastapi import APIRouter

router = APIRouter()

@router.get("/v1/health")
def health_check():
    return {
        "message": "API is healthy and running!"
    }