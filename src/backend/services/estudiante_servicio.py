from sqlalchemy.orm import Session
from ..models.estudiante_model import EstudianteModel
from ..schemas.estudiante import EstudianteCreate

class EstudianteServicio:

    @staticmethod
    def guardar(db: Session, estudianteNuevo: EstudianteCreate):
        nuevo = EstudianteModel(
            nombre=estudianteNuevo.nombre,
            apellido=estudianteNuevo.apellido,
            email=estudianteNuevo.email
        )
        db.add(nuevo)
        db.commit()         
        db.refresh(nuevo)    
        return nuevo
        
    @staticmethod
    def mostrar(db: Session):
        return db.query(EstudianteModel).all()

    @staticmethod
    def actualizar(db: Session, id: int, estudiante: EstudianteCreate):
        estudiante_db = db.query(EstudianteModel).filter(EstudianteModel.id == id).first()
        if estudiante_db:
            estudiante_db.nombre = estudiante.nombre
            estudiante_db.apellido = estudiante.apellido
            estudiante_db.email = estudiante.email
            db.commit()
            db.refresh(estudiante_db)
            return estudiante_db
        return None

    @staticmethod
    def eliminar(db: Session, id: int):
        estudiante_db = db.query(EstudianteModel).filter(EstudianteModel.id == id).first()
        if estudiante_db:
            db.delete(estudiante_db)
            db.commit()
            return id
        return None