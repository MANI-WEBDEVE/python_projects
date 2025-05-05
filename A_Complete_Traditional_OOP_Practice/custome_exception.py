 
class InvalidPasswordError(Exception):
    """Custom exception for invalid password."""
    def __init__(self, message="Password must be at least 8 characters long and contain at least one number."):
        self.message = message
        super().__init__(self.message)

def password_validator(password):
    """Validate the password."""
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise InvalidPasswordError()
    return True


try:
    password = input("Enter your password: ")
    password_validator(password)
    print("Password is valid.")
except InvalidPasswordError as e:
    print(e.message)