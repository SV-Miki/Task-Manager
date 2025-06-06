from enum import Enum
from datetime import datetime
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
        self._title = title
        self._deadline = deadline
        self._status = status
        self._created_at = datetime.now()

    @property
    def title(self) -> str:
        """Название задачи."""
        return self._title

    @property
    def deadline(self) -> Optional[datetime]:
        """Дата дедлайна задачи."""
        return self._deadline

    @property
    def status(self) -> TaskStatus:
        """Статус задачи."""
        return self._status

    @status.setter
    def status(self, new_status: TaskStatus) -> None:
        """Меняет статус задачи."""
        self._status = new_status

    @property
    def created_at(self) -> datetime:
        """Дата и время создания задачи."""
        return self._created_at

    @property
    def is_overdue(self) -> bool:
        """True, если задача просрочена и ещё не выполнена."""
        if self._deadline is None:
            return False
        return datetime.now() > self._deadline and self._status != TaskStatus.DONE

    def __str__(self) -> str:
        """Строковое представление задачи для вывода в консоль."""
        deadline_str = (
            self._deadline.strftime(DATE_DISPLAY_FORMAT)
            if self._deadline
            else "Без дедлайна"
        )
        return f"[{self._status.value}] {self._title} — срок до {deadline_str}"

    def __eq__(self, other: Any) -> bool:
        """Задачи равны, если совпадают название и дата создания."""
        if not isinstance(other, Task):
            return False
        return self.title == other.title and self.created_at == other.created_at