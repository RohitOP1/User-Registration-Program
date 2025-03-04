import re

def validate_password_uc8(password):
    # Rule 4: Has exactly 1 special character
    if not re.search(r'^[^!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?]*[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?][^!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?]*$', password):
        return False
    return True

# Test
password = input("Enter Password: ")
print("Password is valid for UC8:", validate_password_uc8(password))

