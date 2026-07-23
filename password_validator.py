import re

def check_password_validity():
    # Prompt the user for a comma-separated sequence of passwords
    input_data = input("Enter the passwords separated by comma: ")
    
    # Split the input string into individual passwords
    passwords = input_data.split(",")
    
    valid_passwords = []
    
    for password in passwords:
        # Strip any accidental leading/trailing whitespaces around the password
        password = password.strip()
        
        # 1. Check length restrictions (6 to 12 characters inclusive)
        if len(password) < 6 or len(password) > 12:
            continue
            
        # 2. Check for at least 1 lowercase letter [a-z]
        if not re.search("[a-z]", password):
            continue
            
        # 3. Check for at least 1 uppercase letter [A-Z]
        if not re.search("[A-Z]", password):
            continue
            
        # 4. Check for at least 1 numeric digit [0-9]
        if not re.search("[0-9]", password):
            continue
            
        # 5. Check for at least 1 special character from [$#@]
        if not re.search("[$#@]", password):
            continue
            
        # If all criteria match, add to the valid list
        valid_passwords.append(password)
        
    # Print the valid passwords joined together by commas
    print(",".join(valid_passwords))

# Execute the function
if __name__ == "__main__":
    check_password_validity()
