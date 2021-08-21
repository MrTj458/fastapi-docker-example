from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Todo(models.Model):
    id = fields.IntField(pk=True)
    desc = fields.TextField()
    completed = fields.BooleanField()

Todo_Pydantic = pydantic_model_creator(Todo, name='Todo')
TodoIn_Pydantic = pydantic_model_creator(Todo, name='TodoIn', exclude_readonly=True)
