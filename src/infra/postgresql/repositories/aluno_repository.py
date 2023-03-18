from typing import List
from infra.postgresql.config.database import async_session
from domain.models.aluno_model import AlunoModel
from sqlmodel import select


class AlunoRepository:

    async def adicionar(aluno_adicionar: AlunoModel) -> AlunoModel:
        async with async_session() as session:
            session.add(aluno_adicionar)
            await session.commit()

            return aluno_adicionar

    async def deletar(aluno_deletar: AlunoModel) -> None:
        async with async_session() as session:
            await session.delete(aluno_deletar)
            await session.commit()

    async def atualizar(aluno_atualizar: AlunoModel) -> AlunoModel:
        async with async_session() as session:
            query = select(AlunoModel).filter(
                AlunoModel.id == aluno_atualizar.id)
            query_result = await session.execute(query)
            aluno_db: AlunoModel = query_result.scalar_one_or_none()

            if not aluno_db:
                return None

            aluno_db.nome = aluno_atualizar.nome
            aluno_db.idade = aluno_atualizar.idade
            aluno_db.turma_id = aluno_atualizar.turma_id
            await session.commit()

            return aluno_db

    async def obter_todos() -> List[AlunoModel]:
        async with async_session() as session:
            query = select(AlunoModel)
            query_result = await session.execute(query)
            alunos_response: List[AlunoModel] = query_result.scalars().all()

            return alunos_response

    async def obter_por_aluno_id(aluno_id_obter: int) -> AlunoModel:
        async with async_session() as session:
            query = select(AlunoModel).filter(AlunoModel.id == aluno_id_obter)
            query_result = await session.execute(query)
            aluno_db: AlunoModel = query_result.scalar_one_or_none()
            return aluno_db
