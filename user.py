import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9]+([._+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}(\.[a-zA-Z]{2})?$'
    return bool(re.match(pattern, email))

# Test
email = input("Enter Email: ")
print("Email is valid:", validate_email(email))

