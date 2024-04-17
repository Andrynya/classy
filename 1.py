class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_as_completed(self, task_index):
        if task_index < len(self.tasks):
            self.tasks[task_index].completed = True
        else:
            print("Task index out of range.")

    def show_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task.completed]
        if incomplete_tasks:
            for index, task in enumerate(incomplete_tasks):
                print(f"Task {index+1}: {task.description} (Deadline: {task.deadline})")
        else:
            print("No incomplete tasks.")

# Создаем менеджер задач
task_manager = TaskManager()

# Добавляем задачи
task1 = Task("Сделать уроки", "15.09.2021")
task2 = Task("Сходить в магазин", "20.09.2021")
task_manager.add_task(task1)
task_manager.add_task(task2)

# Отмечаем первую задачу как выполненную
task_manager.mark_as_completed(0)

# Выводим текущие (не выполненные) задачи
print("Текущие (не выполненные) задачи:")
task_manager.show_incomplete_tasks()