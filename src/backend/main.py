from fastapi import FastAPI
from .apis.estudiante_api import router
from .apis.home_api import router as home_router


app = FastAPI()
app.include_router(home_router)
app.include_router(router=router, prefix='/api')