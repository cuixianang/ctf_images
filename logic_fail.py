# logic_fail.py

# This function is supposed to check if the correct number exists and decode the flag

import base64

def find_flag(numbers):
    encoded_flag = "SUdOSVRFe3R5cGVfZml4X3Bhc3NlZH0="  
    for num in number:
        if num == "42":  
            return base64.b64decode(encoded_flag).encode()
    return "No flag found."

data = ["13", 7, "twenty", 42, "99"]
print(find_flag(data))
