from task import Task
from storage import Storage

class TaskManager:
    def __init__(self):
        self.tasks = Storage.load_tasks()

    def add_task(self, title, priority, due):
        task = Task(title, priority, due)
        self.tasks.append(task)
        Storage.save_tasks(self.tasks)
        print("Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
           print("Nothing to show.")
           return
    
        for i, task in enumerate(self.tasks, start = 1):
            status = "Completed" if task.completed else "Not Completed"
            due = task.due if task.due else "No due date"
            overdue = "Overdue" if task.is_overdue() else ""    
            print(
                f"{i}.{task.title} |{task.priority.upper()} | {due}[{status}]{overdue}")

    def is_valid_task_number(self, number):
        return 1 <= number <= len(self.tasks)    

    def complete_task(self, number):
        if not self.tasks:
            print(" No tasks available.")
            return
        
        if not self.is_valid_task_number(number):
              print("Invalid task number.")
              return

        self.tasks[number - 1].mark_completed()
        Storage.save_tasks(self.tasks)
        print("Task marked as completed!")

    def delete_task(self, number):
        if not self.tasks:
           print("No tasks to delete.")
           return
        
        if not self.is_valid_task_number(number):
            print("Invalid task number.")
            return
    
        self.tasks.pop(number - 1)
        Storage.save_tasks(self.tasks)
        print("Task deleted successfully.")
