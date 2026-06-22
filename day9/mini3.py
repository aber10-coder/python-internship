import streamlit as st

st.title("Registration Form")

with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0)

    submit = st.form_submit_button("Submit")

if submit:

    if "@" not in email:
        st.error("Invalid email address")

    elif age <= 0:
        st.error("Age must be greater than 0")

    else:
        st.success("Form submitted successfully!")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")