import streamlit as st
import auth
import sidebar
st.title("Submit Your Growth Mindset Entry")

# Check if user is logged in
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("You need to log in first!")
    st.stop()  # Stop execution if not logged in


username = st.session_state["username"]
sidebar.show_sidebar()


message = st.text_area("Share your growth mindset experience")

if st.button("Submit"):
    if message:
        data = auth.load_data()
        data["entries"].append({"username": username, "message": message})
        auth.save_data(data)
        st.success("Entry submitted successfully!")
        st.rerun()
    else:
        st.error("Please write something before submitting.")

st.subheader("Your Growth Mindset Entries")

data = auth.load_data()
user_entries = [entry for entry in data["entries"] if entry["username"] == username]

if user_entries:
    for entry in reversed(user_entries):  # Show latest first
        with st.expander(entry["message"]):
            st.write(f"✍️ {entry['message']}")
else:
    st.info("No entries found. Start sharing your mindset journey! 🚀")
