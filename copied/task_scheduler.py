# task_scheduler.py

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Callable, List, Protocol
import threading
import logging

# --- Setup logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Domain Entity ---
@dataclass(frozen=True)
class Task:
    name: str
    execute_at: datetime
    action: Callable[[], None]

# --- TaskValidator ---
class TaskValidationError(Exception):
    pass

class TaskValidator:
    @staticmethod
    def validate(task: Task) -> None:
        if not task.name:
            raise TaskValidationError("Task must have a name.")
        if task.execute_at <= datetime.now():
            raise TaskValidationError("Task time must be in the future.")
        if not callable(task.action):
            raise TaskValidationError("Task action must be callable.")

# --- TaskRepository Protocol (Dependency Inversion) ---
class TaskRepository(Protocol):
    def add(self, task: Task) -> None: ...
    def get_all(self) -> List[Task]: ...

# --- In-Memory Implementation ---
class InMemoryTaskRepository:
    def __init__(self):
        self._tasks: List[Task] = []

    def add(self, task: Task) -> None:
        self._tasks.append(task)

