from tkinter import Tk

from gui import TaskManagerApp


def main():
    root = Tk()
    app = TaskManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
