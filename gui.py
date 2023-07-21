import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

sg.theme('DarkTeal9')

clock = sg.Text('', key = 'clock')
label = sg.Text('Enter a to-do')
textbox = sg.InputText(tooltip='To-Do', key = 'todo')

add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')

list_box = sg.Listbox(values= functions.get_todos(),
                      key = 'todos',
                      enable_events=True,
                      size = [35,10]  )

window = sg.Window('To-Do', 
                    layout = [[clock],
                              [label], 
                              [textbox, add_button],
                              [list_box, edit_button, complete_button]], 
                    #size = (700,500), 
                    font = ('Helvetica',10))

while True:
    event, values = window.read(timeout = 200)
    window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    # print(values['todos'])
    if event == 'Add':
        todos = functions.get_todos()
        new_todo = values['todo'] + '\n'
        todos.append(new_todo.title())
        functions.write_todos('todos.txt', todos)
        window['todos'].update(values = todos)
        window['todo'].update('')
    
    if event == 'Edit':
        try:
            to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = functions.get_todos()
            index = todos.index(to_edit)
            print(index)
            todos[index] = new_todo.title()
            print(todos[index])
            functions.write_todos('todos.txt', todos)
            window['todos'].update(values = todos)
            window['todo'].update('')
        
        except IndexError:
            sg.popup('Select an item first',title='Error', font = ('Helvetica',10) )

    if event == 'Complete':
        try:
            to_complete = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(to_complete)
            todos.pop(index)

            functions.write_todos('todos.txt', todos)
            window['todos'].update(values = todos)
            window['todo'].update('')
        
        except IndexError:
            sg.popup('Select an item first',title='Error', font = ('Helvetica',10) )

    if event == 'todos':
        window['todo'].update(value = values['todos'][0].strip())    

    if event == sg.WIN_CLOSED:
        break

window.close()
