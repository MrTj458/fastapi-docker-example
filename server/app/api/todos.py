from typing import List
from fastapi import APIRouter

from app.models import Todo
from app.models.todo import Todo_Pydantic, TodoIn_Pydantic

from app.schemas.pagination import Page

router = APIRouter(
    prefix='/todos',
    tags=['todos'],
)


@router.get('/', response_model=Page[List[Todo_Pydantic]])
async def get_todos(page: int = 1):
    return Page(page=page, total_pages=1, data=await Todo_Pydantic.from_queryset(Todo.all()))


@router.get('/{todo_id}', response_model=Todo_Pydantic)
async def get_todo(todo_id: int):
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=todo_id))


@router.post('/', status_code=201, response_model=Todo_Pydantic)
async def create_todo(todo: TodoIn_Pydantic):
    todo_obj = await Todo.create(**todo.dict())
    return await Todo_Pydantic.from_tortoise_orm(todo_obj)
