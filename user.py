import re

def validate_name(name):
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    return bool(re.match(pattern, name))

# Test
first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")

print("First Name is valid:", validate_name(first_name))
# print("Last Name is valid:", validate_name(last_name))

