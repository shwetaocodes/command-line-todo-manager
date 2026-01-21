from datetime import datetime, date

class Task:

    def __init__(self, title, priority = "Medium", due = None, completed= False):
        self.title = title
        self.priority = priority
        self.due = due
        self.completed = completed 

    def mark_complete(self):
        self.complete = True

    def is_overdue(self):
        if self.completed or not self.due:
             return False
        return date.today() > datetime.strptime(self.due, "%Y-%m-%d").date()

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "due": self.due,
            "completed": self.completed
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data.get("priority", "medium"),
            data.get("due"), 
            data.get("completed", False)
            )
