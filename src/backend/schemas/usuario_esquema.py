from pydantic import BaseModel, model_validator

# 1. Lo que RECIBE FastAPI para registrar
class UsuarioRegistro(BaseModel):
    nombres: str
    apellidos: str
    email: str
    telefono: str
    dni: str
    password: str
    confirmar_password: str  # 👈 Cambiado a 'confirmar_password' (igual que en Angular)

    @model_validator(mode="after")
    def verificar_password_coincide(self):
        if self.password != self.confirmar_password:
            raise ValueError("Las contraseñas no coinciden")
        return self

# 2. Lo que RECIBE FastAPI para login
class UsuarioLogin(BaseModel):
    email: str
    password: str

# 3. Lo que DEVUELVE FastAPI al Frontend (Respuesta segura sin contraseñas)
class UsuarioResponse(BaseModel):
    id: int
    nombres: str
    apellidos: str
    email: str
    telefono: str
    dni: str

    class Config:
        from_attributes = True  # 👈 Corregido el typo (le faltaba una 't')