tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def list_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

add_task("Learn Git")
add_task("Build GenAI projects")
list_tasks()