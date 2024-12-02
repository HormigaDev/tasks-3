class TaskPriorities:
    low = "low"
    normal = "normal"
    high = "high"
    urgent = "urgent"

task_priorities = [
    TaskPriorities.low,
    TaskPriorities.normal,
    TaskPriorities.high,
    TaskPriorities.urgent,
]

class TaskStatus:
    open = "open"
    finalized = "completed"
    cancelled = "cancelled"
    archived = "archived"
    current = "current"

task_status = [
    TaskStatus.open,
    TaskStatus.finalized,
    TaskStatus.cancelled,
    TaskStatus.archived,
    TaskStatus.current
]
