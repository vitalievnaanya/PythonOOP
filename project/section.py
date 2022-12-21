from project import task
from project.task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.task = []

    def add_task(self, new_task):
        for task in self.task:
            if task == new_task:
                return f'Task is already in the section {self.name}'
        self.task.append(new_task)

    def complete_task(self, task_name):
        for task in self.task:
            if task == task_name:
                task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        tasks_count = 0

        for task in self.task:
            if task.completed:
                tasks_count += 1
                self.task.remove(task)

        return f'Cleared {tasks_count} tasks.'

    def view_section(self):
        result = f'Section {self.name}'

        for task in self.task:
            result += '\n'
            result += task.details()

        return result

        
