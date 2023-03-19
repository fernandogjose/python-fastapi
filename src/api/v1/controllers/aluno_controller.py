from typing import List
from fastapi import APIRouter, status, HTTPException, Response
from domain.models.aluno_model import AlunoModel
from domain.services.aluno_service import AlunoService


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=AlunoModel)
async def post(aluno_adicionar: AlunoModel):
    aluno_service: AlunoService = AlunoService()
    return await aluno_service.adicionar(aluno_adicionar)


@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=AlunoModel)
async def put(aluno_atualizar: AlunoModel):
    aluno_service: AlunoService = AlunoService()
    aluno_atualizado = await aluno_service.atualizar(aluno_atualizar)

    if not aluno_atualizado:
        raise HTTPException(detail='Aluno não encontrado',
                            status_code=status.HTTP_404_NOT_FOUND)

    return aluno_atualizado


@router.delete('/{aluno_id_deletar}', status_code=status.HTTP_202_ACCEPTED, response_model=int)
async def delete(aluno_id_deletar: int):
    aluno_service: AlunoService = AlunoService()
    aluno_id_deletado = await aluno_service.deletar(aluno_id_deletar)

    if aluno_id_deletado > 0:
        return aluno_id_deletado

    raise HTTPException(detail='Aluno não encontrado',
                        status_code=status.HTTP_404_NOT_FOUND)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[AlunoModel])
async def get():
    aluno_service: AlunoService = AlunoService()
    return await aluno_service.obter_todos()


@router.get('/{aluno_id_obter}', status_code=status.HTTP_200_OK, response_model=AlunoModel)
async def get(aluno_id_obter: int):
    aluno_service: AlunoService = AlunoService()
    aluno_db = await aluno_service.obter_por_aluno_id(aluno_id_obter)

    if aluno_db:
        return aluno_db

    raise HTTPException(detail='Aluno não encontrado',
                        status_code=status.HTTP_404_NOT_FOUND)
