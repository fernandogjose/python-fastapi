from fastapi import FastAPI
from infra.core.application_settings import application_settings
from api.v1.api import api_router

app: FastAPI = FastAPI(title='API da Escola Eco Aprender')
app.include_router(api_router, prefix=application_settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000,
                log_level='info', reload=True)
