import json
import datetime as dt

from utils import datetime_handler


class Task():

    def __init__(self, task_id, task_title):
        self.task_id = task_id
        self.task_title = task_title
        self.status = 'Active'
        self.created_at = dt.datetime.now()

    def __str__(self):
        return f"Task(id={self.task_id}, title='{self.task_title}, status='{self.status}, created_at='{self.created_at}')"


class TaskManager():

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        print(self.tasks)
        self.next_id += 1
        self.save_to_file()
        print('Задача добавлена!')

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_to_file()

    def change_status(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = 'Inactive'
                break
        self.save_to_file()

    def change_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.task_title = input('Введите измененную тему: ')
                break
        self.save_to_file()

    def all_tasks(self):
        for task in self.tasks:
            print(task)

    def save_to_file(self):
        with open("tasks.json", "w") as file:
            json.dump([task.__dict__ for task in self.tasks],
                      file, indent=4, default=datetime_handler)

    def load_from_file(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
                self.tasks = [
                    Task(task["task_id"],
                         task["task_title"],
                         task["created_at"]) for task in data
                    ]
                if self.tasks:
                    self.next_id = max(task.task_id for task in self.tasks) + 1
        except FileNotFoundError:
            self.tasks = []
