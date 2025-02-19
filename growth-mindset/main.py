import streamlit as st
import auth  
import sidebar
st.set_page_config(page_title="Growth Mindset App")

# Session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
sidebar.show_sidebar()
st.title("Welcome to Growth Mindset Web App")
st.warning("For your safety, please do not share any personal information here. Use only random usernames and passwords for login and sign up.")
# Authentication UI
if not st.session_state["authenticated"]:
    st.subheader("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, message = auth.sign_in(username, password)
        if success:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.rerun()
        else:
            st.error(message)

    st.subheader("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        success, message = auth.sign_up(new_username, new_password)
        if success:
            st.success(message)
        else:
            st.error(message)

else:
    st.success(f"Welcome, {st.session_state['username']}! 🎉")
    if st.button("Submit an Entry"):
        st.switch_page("pages/submit-entry.py")  # Redirect to Submit Entry page
    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()
