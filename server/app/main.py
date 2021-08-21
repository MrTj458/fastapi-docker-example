import os
from fastapi import FastAPI, Depends
from app.config import Settings, get_settings

from app.api.todos import router

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

register_tortoise(
    app,
    db_url=os.getenv('DATABASE_URL'),
    modules={'models': ['app.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(router)


@app.get('/')
async def index(settings: Settings = Depends(get_settings)):
    return {
        'msg': 'Hello from FastAPI!',
        'database_url': settings.database_url
    }
