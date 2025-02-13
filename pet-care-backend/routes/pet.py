from fastapi import APIRouter

router = APIRouter()

@router.get("/pets")
def get_pets():
    return {"message": "Pet profiles"}
