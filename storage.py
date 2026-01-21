import json
import os
from task import Task

class Storage:
    file_name = "tasks.json"

    @staticmethod
    def load_tasks():
        if not os.path.exists(Storage.file_name):
            return []
        try:
            with open(Storage.file_name, "r") as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data] 
        except json.JSONDecodeError:
            print("Corrupted tasks file. Starting fresh.")  
            return []
        
    @staticmethod
    def save_tasks(tasks):
        with open(Storage.file_name, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)
