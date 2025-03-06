import re
import streamlit as st
import json
import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerics = '1234567890'
symbols = '!@#$%^&*_+;:.<>?'

def generate_password(length):
    if length < 8:
        return "Password length should be at least 8 characters."
    
    password = []
    password.append(random.choice(alphabet.lower()))
    password.append(random.choice(alphabet.upper()))
    password.append(random.choice(numerics))
    password.append(random.choice(symbols))
    
    while len(password) < length:
        password.append(random.choice(alphabet + numerics + symbols))
    
    random.shuffle(password)
    return ''.join(password)

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        return "❌ Password should be at least 8 characters long."
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        return "❌ Include both uppercase and lowercase letters."
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        return "❌ Add at least one number (0-9)."
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        return "❌ Include at least one special character (!@#$%^&*)."
    
    # Additional Checks
    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password) and re.search(r"[!@#$%^&*]", password):
        score += 1
    
    # Strength Rating
    if score >= 5:
        return "✅ Very Strong Password!"
    elif score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "❌ Weak Password - Improve it using the suggestions above."

# Set the page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Set the page title
st.title("Password Strength Checker")
st.write("Enter your password to check its strength:")
pass_history = []
password = st.text_input("Enter Your Password", type="password")

col1, col2 = st.columns(2)
with col2:
    if st.button("Generate a Password"):
        pass_len = 12
        st.code(generate_password(pass_len))
with col1:
    if st.button("Check Password Strength", type="primary"):
        validate = check_password_strength(password)
        if "✅" in validate:
            st.success(validate)
        else:
            st.error(validate)

        # Load existing password history from the JSON file
        try:
            with open("password.json", 'r') as f:
                pass_history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass_history = []

        # Write the updated password history back to the JSON file
        with open("password.json", 'w') as f:
            if "✅" in validate:
                # Append the new password to the history
                pass_history.append(password)
            json.dump(pass_history, f)
        
        st.write("Password History:")
        for i in pass_history:
            st.code(i)
