from ..schemas.usuario_esquema import UsuarioRegistro
from sqlalchemy.orm import Session
from ..models.usuario_model import UsuarioModel
class UsuarioRepository:
    def __init__(self,db : Session):
        self.db = db

    def obtener_usuario_por_email(self, email: str) -> UsuarioModel | None:
        return self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()
    
    def obtener_usuario_por_dni(self, dni: str) -> UsuarioModel | None  :
        return self.db.query(UsuarioModel).filter(UsuarioModel.dni == dni).first()
    
    def crear_usuario(self, usuario_datos: UsuarioRegistro , password_hashed: str)-> UsuarioModel:
        db_usuario =UsuarioModel(
            nombres =usuario_datos.nombres,
            apellidos=usuario_datos.apellidos,
            email=usuario_datos.email,
            telefono=usuario_datos.telefono,
            dni=usuario_datos.dni,
            password_hash=password_hashed
        )
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
        

