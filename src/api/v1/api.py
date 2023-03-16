from fastapi import APIRouter
from api.v1.controllers import aluno_controller

api_router = APIRouter()
api_router.include_router(aluno_controller.router,
                          prefix='/alunos',
                          tags=['alunos'])
