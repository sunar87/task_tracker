from tkinter import Tk, Label, Entry, Button, Text, Listbox, messagebox, END, Toplevel
from task import TaskManager


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Менеджер задач')
        self.task_manager = TaskManager()

        self.label = Label(root, text='Введите задачу:')
        self.label.pack()

        self.entry = Entry(root, width=50)
        self.entry.pack()

        self.add_button = Button(
            root, text='Добавить задачу', command=self.add_task
            )
        self.add_button.pack()

        self.task_listbox = Listbox(root, width=50)
        self.task_listbox.pack()

        self.delete_button = Button(
            root, text='Удалить задачу', command=self.delete_task
            )
        self.delete_button.pack()

        self.change_status_button = Button(
            root, text='Изменить статус', command=self.change_status
            )
        self.change_status_button.pack()

        self.change_title_button = Button(
            root, text='Изменить задачу', command=self.change_task
            )
        self.change_title_button.pack()

        self.show_all_button = Button(
            root, text='Показать все задачи', command=self.show_all_tasks
            )
        self.show_all_button.pack()

        self.task_manager.load_from_file()
        self.refresh_tasks()

    def add_task(self):
        title = self.entry.get()
        if title:
            self.task_manager.add_task(title)
            self.entry.delete(0, END)
            self.refresh_tasks()
            messagebox.showinfo('Успех', 'Задача добавлена!')

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_id = int(self.task_listbox.get(selected_task).split(':')[0])
            self.task_manager.delete_task(task_id)
            self.refresh_tasks()
            messagebox.showinfo('Успех', 'Задача удалена!')

    def change_status(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_id = int(self.task_listbox.get(selected_task).split(':')[0])
            self.task_manager.change_status(task_id)
            self.refresh_tasks()
            messagebox.showinfo('Успех', 'Статус задачи изменен!')

    def change_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_id = int(self.task_listbox.get(selected_task).split(':')[0])
            new_title = self.entry.get()
            if new_title:
                self.task_manager.change_task(task_id, new_title)
                self.entry.delete(0, END)
                self.refresh_tasks()
                messagebox.showinfo('Успех', 'Задача изменена!')

    def show_all_tasks(self):
        tasks_window = Toplevel(self.root)
        tasks_window.title('Все задачи')

        tasks_text = Text(tasks_window, width=60, height=20)
        tasks_text.pack()

        tasks = self.task_manager.all_tasks()
        if tasks:
            for task in tasks:
                tasks_text.insert(END, f'ID: {task.task_id}\n')
                tasks_text.insert(END, f'Название: {task.task_title}\n')
                tasks_text.insert(END, f'Статус: {task.status}\n')
                tasks_text.insert(END, f'Дата создания: {task.created_at}\n')
                tasks_text.insert(END, '-' * 40 + '\n')
        else:
            tasks_text.insert(END, 'Задачи отсутствуют.\n')

        tasks_text.config(state='disabled')

    def refresh_tasks(self):
        self.task_listbox.delete(0, END)
        for task in self.task_manager.all_tasks():
            self.task_listbox.insert(END, f"{task.task_id}: {task.task_title} ({task.status})")
