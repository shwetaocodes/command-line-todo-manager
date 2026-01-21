import argparse
from task_manager import TaskManager

def main():
    parser = argparse.ArgumentParser(
        description="Command-line To-Do Manager"
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("--priority", choices = ["low", "medium", "high"], default = "medium", type = str.lower, help = "Task priority (low, medium, high)")
    add_parser.add_argument("--due", help = "Due date (YYYY-MM-DD)")

    subparsers.add_parser("list", help="List all tasks")

    done_parser = subparsers.add_parser("done", help = "Mark task as completed")
    done_parser.add_argument("number", type = int, help = "Task number")

    delete_parser = subparsers.add_parser("delete", help = "Delete a task")
    delete_parser.add_argument("number", type = int, help = "Task number")

    args = parser.parse_args()
    manager = TaskManager()
    

    if args.command == "add":
       manager.add_task(args.title, args.priority, args.due)

    elif args.command == "list":
        manager.list_tasks()

    elif args.command == "done":
        manager.complete_task(args.number)    

    elif args.command == "delete": 
        manager.delete_task(args.number)   

    else:
        parser.print_help()


if __name__ == "__main__":
    main()        