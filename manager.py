from typing import List, Generator, Optional, Iterator
from task import Task


class TaskManager:
    """Класс для управления списком задач"""

    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Добавляет задачу в список"""
        self._tasks.append(task)

    def remove_task(self, index: int) -> bool:
        """Удалить задачу по индексу. Возвращает True, если успешно."""
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)
            return True
        return False

    def get_task_by_index(self, index: int) -> Optional[Task]:
        """Получает задачу по индексу. Если индекса нет — вернуть None."""
        if 0 <= index < len(self._tasks):
            return self._tasks[index]
        return None

    def __len__(self) -> int:
        """Количество задач."""
        return len(self._tasks)

    def __iter__(self) -> Iterator[Task]:
        """Итерирование по задачам."""
        return iter(self._tasks)

    def overdue_tasks(self) -> Generator[Task, None, None]:
        """Генератор по просроченным задачам."""
        for task in self._tasks:
            if task.is_overdue:
                yield task