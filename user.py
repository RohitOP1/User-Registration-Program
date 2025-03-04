import re

def validate_password_uc7(password):
    # Rule 3: Should have at least 1 numeric digit
    if not re.search(r'\d', password):  # \d matches any digit (0-9)
        return False
    return True

# Test
password = input("Enter Password: ")
print("Password is valid for UC7:", validate_password_uc7(password))

