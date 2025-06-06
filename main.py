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

    @staticmethod
    def display_menu() -> None:
        """Отображает главное меню приложения"""
        print("МЕНЕДЖЕР ЗАДАЧ")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Показать просроченные задачи")
        print("4. Изменить статус задачи")
        print("5. Выход")

    def add_task(self) -> None:
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

    def view_tasks(self) -> None:
        """Отображает все задачи"""
        if len(self.manager) == 0:
            print(MSG_LIST_EMPTY)
            return
        for i, task in enumerate(self.manager, 1):
            print(f"{i}. {task}")

    def show_overdue_tasks(self) -> None:
        """Отображает только просроченные задачи"""
        overdue = list(self.manager.overdue_tasks())
        if not overdue:
            print(MSG_NO_OVERDUE)
            return
        print("Просроченные задачи:")
        for task in overdue:
            print(task)

    def change_task_status(self) -> None:
        """Изменяет статус выбранной задачи"""
        if len(self.manager) == 0:
            print(MSG_LIST_EMPTY)
            return
        self.view_tasks()
        try:
            task_num = int(input("Введите номер задачи для смены статуса: "))
        except ValueError:
            print(MSG_INVALID_TASK_NUMBER)
            return
        if not (1 <= task_num <= len(self.manager)):
            print(MSG_INVALID_TASK_NUMBER)
            return
        task = self.manager.get_task_by_index(task_num - 1)
        statuses = list(TaskStatus)
        print("Статусы:")
        for i, status in enumerate(statuses, 1):
            print(f"{i}. {status.value}")
        try:
            status_num = int(input("Выберите новый статус: "))
        except ValueError:
            print(MSG_INVALID_STATUS)
            return
        if not (1 <= status_num <= len(statuses)):
            print(MSG_INVALID_STATUS)
            return
        if task:
            task.status = statuses[status_num - 1]
            print("Статус задачи обновлен.")

    def run(self) -> None:
        """Главный цикл приложения"""
        print("Добро пожаловать в Менеджер Задач!")
        while True:
            self.display_menu()
            choice = input("Выберите действие: ").strip()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.show_overdue_tasks()
            elif choice == "4":
                self.change_task_status()
            elif choice == "5":
                print(MSG_EXIT)
                break
            else:
                print(MSG_INVALID_CHOICE)


if __name__ == "__main__":
    cli = TaskManagerCLI()
    cli.run()
