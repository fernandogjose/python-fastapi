from pydantic import BaseSettings


class ApplicationSettings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://admin:admin@localhost:5432/EcoAprender'

    class Config:
        case_sensitive = True


application_settings: ApplicationSettings = ApplicationSettings()
