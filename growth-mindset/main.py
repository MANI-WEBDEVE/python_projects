import streamlit as st
import json
from auth import sign_up, sign_in, load_data, save_data

# Session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

st.title("🌱 Growth Mindset Challenge")

# Navigation Tabs
page = st.sidebar.radio("Navigation", ["Sign In", "Sign Up", "Submit Entry"])

# **🔹 SIGN UP PAGE**
if page == "Sign Up":
    st.subheader("📝 Create an Account")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        success, message = sign_up(new_username, new_password)
        st.success(message) if success else st.error(message)

# **🔹 SIGN IN PAGE**
elif page == "Sign In":
    st.subheader("🔑 Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        success, message = sign_in(username, password)
        if success:
            st.session_state["refresh"] = not st.session_state.get("refresh", False)
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success(message)
            st.rerun()
        else:
            st.error(message)

# **🔹 SUBMIT GROWTH MINDSET ENTRY**
elif page == "Submit Entry":
    if not st.session_state["authenticated"]:
        st.warning("⚠️ Please Sign In to submit an entry.")
        st.stop()

    st.subheader(f"📖 Welcome, {st.session_state['username']}!")
    mindset_entry = st.text_area("How do you practice a Growth Mindset?")

    if st.button("Submit Entry"):
        if mindset_entry:
            data = load_data()
            data["entries"].append({"username": st.session_state["username"], "entry": mindset_entry})
            save_data(data)
            st.success("✅ Entry submitted successfully!")
        else:
            st.warning("⚠️ Please enter your response before submitting.")

# **🔹 DISPLAY PAST ENTRIES**
st.sidebar.subheader("📜 Past Entries")
data = load_data()
for entry in data["entries"]:
    st.sidebar.text(f"📝 {entry['username'].split('@')[0]}: {entry['entry'][:50]}...")
