from pydantic import BaseModel, EmailStr

# Datos básicos para crear / actualizar
class EstudianteCreate(BaseModel):
    nombre: str
    apellido: str
    email: str

# Datos para responder al cliente (incluye el ID generado por SQL Server)
class EstudianteResponse(EstudianteCreate):
    id: int 

    class Config:
        from_attributes = True  # Para leer los modelos de SQLAlchemy