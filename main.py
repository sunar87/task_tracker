from task import TaskManager


def main():
    manager = TaskManager()
    manager.load_from_file()

    while True:
        print("\nДобро пожаловать в To-Do List!")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Изменить задачу")
        print("5. Удалить задачу")
        print("6. Выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            manager.all_tasks()
        elif choice == "2":
            title = input("Введите название задачи: ")
            manager.add_task(title)
        elif choice == "3":
            task_id = int(input("Введите ID задачи: "))
            manager.change_status(task_id)
        elif choice == "4":
            task_id = int(input("Введите ID задачи: "))
            manager.change_task(task_id)
        elif choice == "5":
            task_id = int(input("Введите ID задачи: "))
        elif choice == "6":
            break
        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
