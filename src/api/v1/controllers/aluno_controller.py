from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from models.aluno_model import AlunoModel
from core.deps import get_session

# bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar
Select.inherit_cache = True
SelectOfScalar.inherit_cache = True


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=AlunoModel)
async def post(aluno_request: AlunoModel, db: AsyncSession = Depends(get_session)):
    aluno_adicionar = AlunoModel(nome=aluno_request.nome,
                                 idade=aluno_request.idade,
                                 turma_id=aluno_request.turma_id)

    db.add(aluno_adicionar)
    await db.commit()

    return aluno_adicionar


@router.put('/{aluno_id}', status_code=status.HTTP_202_ACCEPTED, response_model=AlunoModel)
async def get(aluno_id: int, aluno_request: AlunoModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        query_result = await session.execute(query)
        aluno_db: List[AlunoModel] = query_result.scalar_one_or_none()

        if aluno_db:
            aluno_db.nome = aluno_request.nome
            aluno_db.idade = aluno_request.idade
            aluno_db.turma_id = aluno_request.turma_id

            await session.commit()
            return aluno_db
        else:
            raise HTTPException(detail='Aluno não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{aluno_id}', status_code=status.HTTP_202_ACCEPTED, response_model=int)
async def get(aluno_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        query_result = await session.execute(query)
        aluno_db: List[AlunoModel] = query_result.scalar_one_or_none()

        if aluno_db:
            await session.delete(aluno_db)
            await session.commit()
            return aluno_id
        else:
            raise HTTPException(detail='Aluno não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[AlunoModel])
async def get(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel)
        query_result = await session.execute(query)
        alunos_response: List[AlunoModel] = query_result.scalars().all()

        return alunos_response


@router.get('/{aluno_id}', status_code=status.HTTP_200_OK, response_model=AlunoModel)
async def get(aluno_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        query_result = await session.execute(query)
        aluno_db: List[AlunoModel] = query_result.scalar_one_or_none()

        if aluno_db:
            return aluno_db
        else:
            raise HTTPException(detail='Aluno não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)
