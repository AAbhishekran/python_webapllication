import streamlit as st
import function
todos = function.file()
def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    function.write(todos)
    # print(todo)
# file=st.text_input("Plz enter your file name")l


st.title("this is my todos aap")
st.write("hello")
st.subheader("This app increase your productivity in the future problem ")
for check in todos:
    st.checkbox(check)

st.text_input(label="" , placeholder="Add new todos ",
              on_change=add_todo, key="new_todo")