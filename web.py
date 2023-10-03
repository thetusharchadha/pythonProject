import streamlit as st
import functions

todos = functions.file_read('todo.txt')
def add_todo():
    new_todo=st.session_state['new_todo']+'\n'
    todos.append(new_todo)
    functions.file_write(todos,'todo.txt')

st.title('My Todo App')

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.file_write(todos,'todo.txt')
        st.rerun()
st.text_input(label="Please enter a new todo", placeholder='Add a new todo....'
              ,on_change=add_todo, key='new_todo')
