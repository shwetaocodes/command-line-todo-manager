# Command-Line To-Do Manager (Python)

This project is a Python-based command-line To-Do Manager that leverages argparse and Object-Oriented Programming to provide a clean, maintainable, and user-friendly CLI experience.

## Features

- **Task Creation** - Add tasks with customizable priority levels and due dates
- **Task Listing** - View all tasks with their current status at a glance
- **Task Completion** - Mark tasks as completed to track your progress
- **Persistent Storage** - Automatic JSON-based storage for data persistence
- **Modular Architecture** - Clean separation of concerns for maintainability

## Technology Stack

- **Python 3.x** - Core programming language
- **argparse** - Command-line argument parsing
- **json** - Data serialization and storage
- **CLI** - Cross-platform terminal interface

## Project Structure

```
CommandLineProject/
│
├── main.py              # Application entry point and CLI interface
├── task_manager.py      # Core task management operations
├── storage.py           # JSON persistence layer
├── task.py              # Task model and data structure
├── tasks.json           # Data storage (auto-generated)
└── README.md            # Documentation
```

### Architecture

| Component | Responsibility |
|-----------|---------------|
| `main.py` | Parses command-line arguments and routes commands |
| `task.py` | Defines the Task class with properties (title, priority, due date, status) |
| `task_manager.py` | Implements business logic for task operations |
| `storage.py` | Handles file I/O operations for task persistence |


### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/CommandLineProject.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd CommandLineProject
   ```

3. **Verify installation**
   ```bash
   python main.py --help
   ```

## Usage

### Add a Task

Create a new task with optional priority and due date parameters.

```bash
python main.py add "Prepare for Interview" --priority High --due 2025-02-01
```

**Output:**
```
✓ Task added successfully.
```

### List All Tasks

Display all tasks with their details and completion status.

```bash
python main.py list
```

**Output:**
```
1. Prepare for Interview | HIGH | 2025-02-01 [Not Completed]
2. Review Python Documentation | MEDIUM | 2025-02-05 [Not Completed]
```

### Mark Task as Completed

Update a task's status to completed using its ID.

```bash
python main.py complete 1
```

**Output:**
```
✓ Task marked as completed.
```

### Command Reference

| Command | Description | Syntax |
|---------|-------------|--------|
| `add` | Create a new task | `python main.py add "<title>" [--priority <level>] [--due <date>]` |
| `list` | Display all tasks | `python main.py list` |
| `complete` | Mark task as done | `python main.py complete <task_id>` |

## Configuration

### Priority Levels

The application supports three priority levels:
- `High` - Urgent and important tasks
- `Medium` - Regular tasks (default)
- `Low` - Nice-to-have tasks

### Date Format

Due dates should be specified in ISO format: `YYYY-MM-DD`

Example: `2025-02-01`

### License

Open Source
