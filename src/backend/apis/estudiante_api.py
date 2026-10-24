from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Rutas adaptadas a tus nombres exactos de archivo
from ..database.conection import get_db
from ..schemas.estudiante import EstudianteCreate, EstudianteResponse
from ..services.estudiante_servicio import EstudianteServicio

router = APIRouter(prefix="/estudiante", tags=["Estudiantes"])

@router.get("/", response_model=List[EstudianteResponse])
def mostrar(db: Session = Depends(get_db)):
    return EstudianteServicio.mostrar(db)

@router.post("/", response_model=EstudianteResponse, status_code=status.HTTP_201_CREATED)
def guardar(estudianteNuevo: EstudianteCreate, db: Session = Depends(get_db)):
    return EstudianteServicio.guardar(db, estudianteNuevo)

@router.put("/{id}", response_model=EstudianteResponse)
def actualizar(id: int, estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    resultado = EstudianteServicio.actualizar(db, id, estudiante)
    if not resultado:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return resultado

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    resultado = EstudianteServicio.eliminar(db, id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return {"mensaje": f"Estudiante con ID {id} eliminado correctamente"}