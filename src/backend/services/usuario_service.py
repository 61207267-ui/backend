from fastapi import HTTPException, status
from ..repositories.usuario_repository import UsuarioRepository 
from ..schemas.usuario_esquema import UsuarioRegistro, UsuarioLogin
from ..models.usuario_model import UsuarioModel
from ..core.segurity import hash_password, verificar_password
class UsuarioService:
    def __init__(self, usuario_repositorio : UsuarioRepository):
        self.usuario_repositorio = usuario_repositorio

    def registrar_usuario(self,datos_usuario: UsuarioRegistro)-> UsuarioModel:
        if self.usuario_repositorio.obtener_usuario_por_email(datos_usuario.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo electrónico ya está registrado")
    
        if self.usuario_repositorio.obtener_usuario_por_dni(datos_usuario.dni):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El DNI ya está registrado")


        clave_encriptada = hash_password(datos_usuario.password)

        return self.usuario_repositorio.crear_usuario(datos_usuario, clave_encriptada)

    def iniciar_sesion(self, datos_login: UsuarioLogin)-> UsuarioModel:
        usuario = self.usuario_repositorio.obtener_usuario_por_email(datos_login.email)

        if not usuario :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Correo electrónico o contraseña incorrectos ")

        es_clave_correcta = verificar_password(datos_login.password, usuario.password_hash)

        if not es_clave_correcta:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Correo electrónico o contraseña incorrectos ")

        return usuario