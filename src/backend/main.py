from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .apis.usuario_api import usuario_router

app = FastAPI(title="API Clínica Pariona")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(usuario_router, prefix="/api")