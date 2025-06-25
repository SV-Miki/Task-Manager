from datetime import datetime

from constants import (DATE_INPUT_FORMAT, MSG_EMPTY_TITLE, MSG_EXIT,
                       MSG_INVALID_CHOICE, MSG_INVALID_DATE,
                       MSG_INVALID_STATUS, MSG_INVALID_TASK_NUMBER,
                       MSG_LIST_EMPTY, MSG_NO_OVERDUE, MSG_TASK_ADDED)
from manager import TaskManager
from task import Task, TaskStatus


class TaskManagerCLI:
    """Класс для работы с командной строкой приложения управления задачами"""

    def __init__(self):
        self.manager = TaskManager()

    def _display_menu(self) -> None:
        """Отображает главное меню приложения"""
        print("МЕНЕДЖЕР ЗАДАЧ")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Показать просроченные задачи")
        print("4. Изменить статус задачи")
        print("5. Выход")

    def _add_task(self) -> None:
        """Добавляет новую задачу через пользовательский ввод"""
        title = input("Введите название:").strip()
        if not title:
            print(MSG_EMPTY_TITLE)
            return
        deadline_str = input("Дедлайн (дд.мм.гггг): ").strip()
        deadline = None
        if deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, DATE_INPUT_FORMAT)
            except ValueError:
                print(MSG_INVALID_DATE)
                return
        task = Task(title=title, deadline=deadline, status=TaskStatus.TODO)
        self.manager.add_task(task)
        print(MSG_TASK_ADDED.format(title=title))

    def _view_tasks(self) -> None:
        """Отображает все задачи"""
        if len(self.manager) == 0:
            print(MSG_LIST_EMPTY)
            return
        for i, task in enumerate(self.manager, 1):
            print(f"{i}. {task}")

    def _show_overdue_tasks(self) -> None:
        """Отображает только просроченные задачи"""
        print("Просроченные задачи:")
        found_overdue = False
        for task in self.manager.overdue_tasks():
            print(task)
            found_overdue = True
        if not found_overdue:
            print(MSG_NO_OVERDUE)

    def _change_task_status(self) -> None:
        """Изменяет статус выбранной задачи"""
        if len(self.manager) == 0:
            print(MSG_LIST_EMPTY)
            return
        self._view_tasks()
        try:
            task_num = int(input("Введите номер задачи для смены статуса: "))
        except ValueError:
            print(MSG_INVALID_TASK_NUMBER)
            return
        task = self.manager.get_task_by_index(task_num - 1)
        if task is None:
            print(MSG_INVALID_TASK_NUMBER)
            return
        print("Выберите новый статус:")
        # Итерируемся напрямую по Enum
        for i, status in enumerate(TaskStatus, 1):
            print(f"{i}. {status.value}")
        try:
            status_num = int(input("Введите номер статуса: "))
        except ValueError:
            print(MSG_INVALID_STATUS)
            return
        # len() работает с Enum, а для получения по индексу создаем список "на лету"
        if not (1 <= status_num <= len(TaskStatus)):
            print(MSG_INVALID_STATUS)
            return
        new_status = list(TaskStatus)[status_num - 1]
        task.status = new_status
        print("Статус задачи обновлен.")

    def run(self) -> None:
        """Главный цикл приложения"""
        print("Добро пожаловать в Менеджер Задач!")
        while True:
            self._display_menu()
            choice = input("Выберите действие: ").strip()
            if choice == "1":
                self._add_task()
            elif choice == "2":
                self._view_tasks()
            elif choice == "3":
                self._show_overdue_tasks()
            elif choice == "4":
                self._change_task_status()
            elif choice == "5":
                print(MSG_EXIT)
                break
            else:
                print(MSG_INVALID_CHOICE)


if __name__ == "__main__":
    cli = TaskManagerCLI()
    cli.run()
