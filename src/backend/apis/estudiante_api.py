from fastapi import APIRouter
from ..services.estudiante_servicio import EstudianteServicio
from ..schemas.estudiante import Estudiante

router = APIRouter(prefix='/estudiante', tags=['Estudiantes'])

estudianteServicio = EstudianteServicio()

@router.post('/')
def guardar(estudianteNuevo: Estudiante):
    return estudianteServicio.guardar(estudianteNuevo=estudianteNuevo)

@router.get('/')
def mostrar():
    return estudianteServicio.mostrar()

@router.put('/{id}')
def actualizar(id: int, estudiante: Estudiante):
    return estudianteServicio.actualizar(id, estudiante)

@router.delete('/{id}')
def eliminar(id: int):
    return estudianteServicio.eliminar(id)