from typing import List
from domain.models.aluno_model import AlunoModel
from infra.postgresql.repositories.aluno_repository import AlunoRepository


class AlunoService:

    def __init__(self, aluno_repository: AlunoRepository = None) -> None:
        self.aluno_repository = aluno_repository or AlunoRepository()

    async def adicionar(self, aluno_adicionar: AlunoModel) -> AlunoModel:
        await self.aluno_repository.adicionar(aluno_adicionar=aluno_adicionar)
        await self.aluno_repository.async_session_commit()
        await self.aluno_repository.async_session_close()

        return aluno_adicionar

    async def deletar(self, aluno_id_deletar: int) -> int:
        aluno_deletar = await self.obter_por_aluno_id(aluno_id_deletar)
        if not aluno_deletar:
            await self.aluno_repository.async_session_close()
            return 0

        await self.aluno_repository.deletar(aluno_deletar)
        await self.aluno_repository.async_session_commit()
        await self.aluno_repository.async_session_close()

        return aluno_id_deletar

    async def atualizar(self, aluno_atualizar: AlunoModel) -> AlunoModel:
        aluno_db = await self.obter_por_aluno_id(aluno_atualizar.id, False)
        if not aluno_db:
            await self.aluno_repository.async_session_close()
            return None

        aluno_db.nome = aluno_atualizar.nome
        aluno_db.idade = aluno_atualizar.idade
        aluno_db.turma_id = aluno_atualizar.turma_id
        await self.aluno_repository.async_session_commit()
        await self.aluno_repository.async_session_close()
        return aluno_db

    async def obter_todos(self) -> List[AlunoModel]:
        alunos = await self.aluno_repository.obter_todos()
        await self.aluno_repository.async_session_commit()
        await self.aluno_repository.async_session_close()
        return alunos

    async def obter_por_aluno_id(self, aluno_id_obter: int, async_session_commit: bool = True) -> AlunoModel:
        aluno_db: AlunoModel = await self.aluno_repository.obter_por_aluno_id(aluno_id_obter)
        if async_session_commit:
            await self.aluno_repository.async_session_commit()
            await self.aluno_repository.async_session_close()

        return aluno_db
