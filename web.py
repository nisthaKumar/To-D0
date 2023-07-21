import functions
import streamlit as st

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'].title()+'\n'
    todos.append(todo)
    functions.write_todos('todos.txt',todos)

todos = functions.get_todos()

st.title('To Do')
#st.subheader('This is my todo app')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos('todos.txt',todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = 'Add new todo', placeholder='Enter a new todo',
               on_change = add_todo,
               key='new_todo')

st.session_state