def get_todos(filepath='todos.txt'):
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos

def write_todos(filepath, todos):
    with open(filepath,'w') as file:
        file.writelines(todos)   