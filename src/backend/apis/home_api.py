from fastapi import APIRouter

router = APIRouter(prefix='/home', tags=['Home'])

@router.get("/")
def read_root():
    return {"status": "ok", "message": "API activa y corriendo"}
