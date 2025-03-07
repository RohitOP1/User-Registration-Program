import re
import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
current_date = datetime.now().strftime("%Y-%m-%d")
log_filename = f"logs/user_registration_{current_date}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def validate_name(name, name_type):
    logger.info(f"Validating {name_type}")
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    if re.match(pattern, name):
        logger.info(f"{name_type} validation successful")
        return True
    logger.warning(f"{name_type} validation failed")
    return False

def validate_email(email):
    logger.info("Validating email")
    pattern = r'^[a-zA-Z0-9]+([._+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}(\.[a-zA-Z]{2})?$'
    if re.match(pattern, email):
        logger.info("Email validation successful")
        return True
    logger.warning("Email validation failed")
    return False

def validate_mobile(mobile):
    logger.info("Validating mobile number")
    pattern = r'^91\s\d{10}$'
    if re.match(pattern, mobile):
        logger.info("Mobile number validation successful")
        return True
    logger.warning("Mobile number validation failed")
    return False

def validate_password(password):
    logger.info("Validating password")
    
    if len(password) < 8:
        logger.warning("Password validation failed: Less than 8 characters")
        return False
    
    if not re.search(r'[A-Z]', password):
        logger.warning("Password validation failed: No uppercase letter")
        return False
    
    if not re.search(r'\d', password):
        logger.warning("Password validation failed: No numeric digit")
        return False
    
    if not re.search(r'^(?=.*[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?])(?!.*[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?].*[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?]).*$', password):
        logger.warning("Password validation failed: Does not have exactly 1 special character")
        return False
    
    logger.info("Password validation successful")
    return True

def main():
    logger.info("Starting user registration validation")

    first_name = input("Enter First Name: ")
    print("First Name is valid:", validate_name(first_name, "First Name"))

    last_name = input("Enter Last Name: ")
    print("Last Name is valid:", validate_name(last_name, "Last Name"))

    email = input("Enter Email: ")
    print("Email is valid:", validate_email(email))

    mobile = input("Enter Mobile Number (91 followed by space and 10 digits): ")
    print("Mobile Number is valid:", validate_mobile(mobile))

    password = input("Enter Password: ")
    print("Password is valid:", validate_password(password))

    logger.info("All validations completed")

if __name__ == "__main__":
    main()
