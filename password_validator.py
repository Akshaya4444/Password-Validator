import re

# The input data is written directly inside the code variable
input_data = "ABd1234@1,a F1#,2w3E*,2We3345"

passwords = [p.strip() for p in input_data.split(",")]
valid_passwords = []

for password in passwords:
    if 6 <= len(password) <= 12:
        if re.search("[a-z]", password) and \
           re.search("[A-Z]", password) and \
           re.search("[0-9]", password) and \
           re.search("[$#@]", password):
            valid_passwords.append(password)

# Output will immediately print: ABd1234@1
print(",".join(valid_passwords))
