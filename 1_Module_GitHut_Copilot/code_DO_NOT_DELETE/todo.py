# Create a class or function to manage a to-do list: add, remove, list tasks
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def list_tasks(self):
        return self.tasks
    
if __name__ == "__main__":  
    todo = TodoList()
    todo.add_task("Buy groceries")
    todo.add_task("Walk the dog")
    print("Current tasks:", todo.list_tasks())
    todo.remove_task("Buy groceries")
    print("Tasks after removal:", todo.list_tasks())
# This code defines a simple TodoList class with methods to add, remove, and list tasks
# It also includes an example usage of the class to demonstrate its functionality.      
