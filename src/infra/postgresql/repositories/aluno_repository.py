from typing import List
from infra.postgresql.config.database import async_session
from domain.models.aluno_model import AlunoModel
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from infra.postgresql.repositories.base_repository import BaseRepository


class AlunoRepository(BaseRepository):

    async def adicionar(self, aluno_adicionar: AlunoModel) -> AlunoModel:
        self.async_session.add(aluno_adicionar)
        return aluno_adicionar

    async def deletar(self, aluno_deletar: AlunoModel) -> None:
        await self.async_session.delete(aluno_deletar)

    async def obter_todos(self) -> List[AlunoModel]:
        query = select(AlunoModel)
        query_result = await self.async_session.execute(query)
        alunos_response: List[AlunoModel] = query_result.scalars().all()
        return alunos_response

    async def obter_por_aluno_id(self, aluno_id_obter: int) -> AlunoModel:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id_obter)
        query_result = await self.async_session.execute(query)
        aluno_db: AlunoModel = query_result.scalar_one_or_none()
        return aluno_db
