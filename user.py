import re

def validate_password_uc5(password):
    # Rule 1: Minimum 8 characters
    if len(password) < 8:
        return False
    return True

# Test
password = input("Enter Password: ")
print("Password is valid for UC5:", validate_password_uc5(password))


