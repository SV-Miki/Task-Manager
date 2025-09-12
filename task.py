from datetime import datetime
from enum import Enum
from typing import Any, Optional

from constants import DATE_DISPLAY_FORMAT


class TaskStatus(Enum):
    """Перечисление возможных статусов задачи"""

    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Task:
    """Класс для представления задачи"""

    def __init__(
        self,
        title: str,
        deadline: Optional[datetime] = None,
        status: TaskStatus = TaskStatus.TODO,
    ) -> None:
        self.title = title
        self.deadline = deadline
        self.status = status
        self._created_at = datetime.now()

    @property
    def created_at(self) -> datetime:
        """Дата и время создания задачи."""
        return self._created_at

    @property
    def is_overdue(self) -> bool:
        """True, если задача просрочена и ещё не выполнена."""
        if self.deadline is None:
            return False
        return datetime.now() > self.deadline and self.status != TaskStatus.DONE

    def __str__(self) -> str:
        """Строковое представление задачи для вывода в консоль."""
        deadline_str = (
            self.deadline.strftime(DATE_DISPLAY_FORMAT)
            if self.deadline
            else "Без дедлайна"
        )
        return f"[{self.status.value}] {self.title} — срок до {deadline_str}"

    def __eq__(self, other: Any) -> bool:
        """Задачи равны, если совпадают название и дата создания."""
        if not isinstance(other, Task):
            return False
        return self.title == other.title and self.created_at == other.created_at
