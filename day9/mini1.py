import streamlit as st

st.title("Greeting App")

if "name" not in st.session_state:
    st.session_state["name"] = ""

name = st.text_input(
    "Enter your name",
    value=st.session_state["name"]
)

if st.button("Greet"):
    st.session_state["name"] = name
    st.success(f"Hello, {st.session_state['name']}!")