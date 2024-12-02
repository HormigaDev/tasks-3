from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_update = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"
