from sqlalchemy import Column, Integer, String
from ..database.base import Base  

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    telefono = Column(String(20), nullable=False)
    dni = Column(String(20), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)