import json
import bcrypt

DATA_FILE = "data.json"

# Load data from JSON
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": [], "entries": []}

# Save data to JSON
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Sign Up Function
def sign_up(username, password):
    data = load_data()

    # Check if user already exists
    for user in data["users"]:
        if user["username"] == username:
            return False, "⚠️ Username already exists. Try another."

    # Hash password before storing
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    # Add new user
    data["users"].append({"username": username, "password": hashed_password})
    save_data(data)
    
    return True, "✅ Account created successfully! You can now login."

# Sign In Function
def sign_in(username, password):
    data = load_data()

    # Check if user exists
    for user in data["users"]:
        if user["username"] == username:
            if bcrypt.checkpw(password.encode(), user["password"].encode()):
                return True, "✅ Login successful!"
            else:
                return False, "❌ Incorrect password. Try again."
    
    return False, "⚠️ User not found. Please sign up."
