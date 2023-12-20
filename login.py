import streamlit as st

def register_user(username, password):
    st.session_state.registered_users[username] = password


def login_user(username, password):
    # Check if the provided username exists and the password matches
    if username in st.session_state.registered_users and st.session_state.registered_users[username] == password:
        return True
    else:
        return False

def ToLogin():
    st.session_state.page = 1

def ToReg():
    st.session_state.page = 2

def ToMain():
    st.session_state.page = 3

# Initialize session_state variables
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}


# Page 1 (Login)
if "page" not in st.session_state:
    st.session_state.page = 1


if st.session_state.page == 1:
    st.title("Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")


    if st.button("Login"):
        if login_user(login_username, login_password):
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

    # Add button to navigate to the Register page
    #if st.button("Go to Register"):
        #st.session_state.page = 2
    st.button('Go to Register', on_click=ToMain())


# Page 2 (Register)
elif st.session_state.page == 2:
    st.title("Register")
    register_username = st.text_input("Username")
    register_password = st.text_input("Password", type="password")


    if st.button("Register"):
        register_user(register_username, register_password)
        st.success("Registration successful!")


        # After registration, navigate back to the Login page
        st.session_state.page = 1


    # Add button to navigate back to the Login page
    #if st.button("Go to Login"):
        #st.session_state.page = 1
    st.button('Go to Login', on_click=ToLogin())

elif st.session_state.page == 3:
    st.title ("Login successful!")
