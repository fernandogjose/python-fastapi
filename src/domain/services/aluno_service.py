from typing import List
from domain.models.aluno_model import AlunoModel
from infra.postgresql.repositories.aluno_repository import AlunoRepository


class AlunoService:

    def __init__(self, aluno_repository: AlunoRepository = None) -> None:
        self.aluno_repository = aluno_repository or AlunoRepository

    async def adicionar(self, aluno_adicionar: AlunoModel) -> AlunoModel:
        return await self.aluno_repository.adicionar(aluno_adicionar=aluno_adicionar)

    async def deletar(self, aluno_id_deletar: int) -> int:
        aluno_deletar = await self.obter_por_aluno_id(aluno_id_deletar)
        if not aluno_deletar:
            return 0

        await self.aluno_repository.deletar(aluno_deletar)
        return aluno_id_deletar

    async def atualizar(self, aluno_atualizar: AlunoModel) -> AlunoModel:
        aluno_atualizado = await self.aluno_repository.atualizar(aluno_atualizar)
        return aluno_atualizado

    async def obter_todos(self) -> List[AlunoModel]:
        return await self.aluno_repository.obter_todos()

    async def obter_por_aluno_id(self, aluno_id_obter: int) -> AlunoModel:
        aluno_db: AlunoModel = await self.aluno_repository.obter_por_aluno_id(aluno_id_obter)
        return aluno_db
