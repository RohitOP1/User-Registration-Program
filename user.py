import re

def validate_mobile(mobile):
    pattern = r'^91\s\d{10}$'
    return bool(re.match(pattern, mobile))

# Test
mobile = input("Enter Mobile Number (91 followed by 10 digits): ")
print("Mobile Number is valid:", validate_mobile(mobile))

