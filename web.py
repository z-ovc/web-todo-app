import streamlit as st
from functions import get_todos,write_todos

todos = get_todos()

def add_todo():
    todo = st.session_state['new_todo']+'\n'
    todos.append(todo)
    write_todos(todos)
    

st.title('my web app')
st.subheader('first advanced app for todo list')
st.write('This app helps you perform better')

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key= todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="enter", placeholder = " enter a todo...",on_change=add_todo ,key='new_todo')
st.session_state