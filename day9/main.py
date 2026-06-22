import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.session_state.setdefault("token", None)
st.session_state.setdefault("email", None)


def show_login():

    st.title("Login")

    with st.form("login_form"):

        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type="password"
        )

        submit = st.form_submit_button("Login")

    if submit:

        try:

            response = requests.post(
                f"{API_URL}/auth/login",
                json={
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state["token"] = data["token"]
                st.session_state["email"] = email

                st.rerun()

            else:

                st.error(
                    response.json()["detail"]
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "FastAPI server is not running"
            )


def show_dashboard():

    st.title("Dashboard")

    st.success(
        f"Welcome {st.session_state['email']}!"
    )

    st.write(
        f"Token: {st.session_state['token']}"
    )

    if st.button("Logout"):

        st.session_state["token"] = None
        st.session_state["email"] = None

        st.rerun()


if st.session_state["token"]:

    show_dashboard()

else:

    show_login()