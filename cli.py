import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        #todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.title() + '\n')

        functions.write_todos('todos.txt', todos)

    elif 'show' in user_action:
        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]
        
        for index, item in enumerate(new_todos):
            print(f"{index+1}-{item}")
        print(len(todos))

    elif 'edit' in user_action:
        try:
        #item_num = int(input("Enter item number to be edited: "))
            item_num = int(user_action[5:])
            new_val = input("Enter new todo: ") + "\n"
            todos[item_num - 1] = new_val.title()

            functions.write_todos('todos.txt', todos)

        except ValueError:
            print("Your command is invalid")
            continue



    elif 'complete' in user_action:
        try:
            #item_num = int(input("Enter item number to be completed: "))
            item_num = int(user_action[9:])
            todos.pop(item_num-1)

            functions.write_todos('todos.txt', todos)
        
        except IndexError:
            print("Item not present at that index")
            continue

    elif 'exit' in user_action:
        break

    else:
        print("Invalid Option")

print("Bye!")