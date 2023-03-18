from infra.postgresql.config.database import async_session
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, async_session_request: AsyncSession = None):
        self.async_session = async_session_request or async_session()

    async def async_session_commit(self) -> None:
        await self.async_session.commit()
        await self.async_session.close()
