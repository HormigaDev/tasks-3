from tortoise import fields
from tortoise.models import Model
from common.enums import task_priorities, TaskPriorities, task_status, TaskStatus

class Task(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    priority = fields.CharEnumField(enum_type=task_priorities, default=TaskPriorities.normal)
    deadline = fields.DatetimeField(null=True)
    status = fields.CharEnumField(enum_type=task_status, default=TaskStatus.open)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_update = fields.DatetimeField(auto_now=True)
    user_id = fields.IntField(index=True)

    class Meta:
        table = "tasks"