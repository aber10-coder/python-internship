import streamlit as st

st.title("Counter App")

if "count" not in st.session_state:
    st.session_state["count"] = 0

if st.button("Increment"):
    st.session_state["count"] += 1

st.metric(
    label="Count",
    value=st.session_state["count"]
)