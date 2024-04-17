class Task():
    def __init__(self, opisanie, srok_vypolnenya):
        self.opisanie = opisanie
        self.srok_vypolnenya = srok_vypolnenya
        self.completed = False

class TaskMenager():
    def __init__(self):
        self.task = []

    def add_task(self, task):
        self.task.append(task) #Добавление в список

    def mark_as_completed(self, task_index):
        if task_index < len(self.task): #Задаём индекс
            self.task[task_index].completed = True
        else:
            print("Индекс задачи выходит за пределы диапазона")

    def incompleted_task(self):
        incompleted_task = [task for task in self.task if not task.completed]
        if incompleted_task: #Определеные не выполненных задач
            for index, task in enumerate(incompleted_task):
                print(f"Задача {index+1}:{task.opisanie} - Срок выполнения: {task.srok_vypolnenya}")
        else:
             print("Нет не выполненных задач")

task_manager = TaskMenager() #Создаём окно задач

task1 = Task("Сделать дз", "16.04.2024")
task2 = Task("Сходить в город", "17.04.2024")
task3 = Task("Доделать реферат", "19.04.2024")
task4 = Task("Побегать", "21.04.2024")

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)
task_manager.add_task(task4)

#Отмечаем выполненнные задачи
task_manager.mark_as_completed(0)
task_manager.mark_as_completed(1)

# Выводим текущие (не выполненные) задачи
print("Текущие (не выполненные) задачи:")
task_manager.incompleted_task()