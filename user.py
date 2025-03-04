import re

def validate_password_uc6(password):
    # Rule 2: Should have at least 1 uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    return True

# Test
password = input("Enter Password: ")
print("Password is valid for UC6:", validate_password_uc6(password))

