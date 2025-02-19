import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.title("Growth Mindset App")
        if "authenticated" in st.session_state and st.session_state["authenticated"]:
            st.write(f"Welcome, {st.session_state['username']}!")
            if st.button("Logout",key='logout-sidebar'):
                st.session_state["authenticated"] = False
                st.rerun()
        else:
            st.write("Please log in to access the app.")
