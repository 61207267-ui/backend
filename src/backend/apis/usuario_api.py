from fastapi import APIRouter,Depends, HTTPException, status    
from sqlalchemy.orm import Session
from ..database.conection import get_db
from ..schemas.usuario_esquema import UsuarioRegistro, UsuarioLogin, UsuarioResponse
from ..repositories.usuario_repository import UsuarioRepository
from ..services.usuario_service import UsuarioService

usuario_router = APIRouter(prefix='/auth', tags=['Autenticación de Usuarios'])


@usuario_router.post('/register' , response_model=UsuarioResponse , status_code=status.HTTP_201_CREATED)
def registrar_usuario(datos:UsuarioRegistro,db:Session = Depends(get_db)):
    repositorio = UsuarioRepository(db)
    servicio = UsuarioService(repositorio)
    return  servicio.registrar_usuario(datos)

@usuario_router.post('/login', response_model=UsuarioResponse , status_code=status.HTTP_200_OK)
def login(datos:UsuarioLogin, db: Session = Depends(get_db)):
    repositorio =UsuarioRepository(db)
    servicio = UsuarioService(repositorio)
    return servicio.iniciar_sesion(datos)