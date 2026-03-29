# Importing the relevant module(s) for the code
import base65

# Creating a function for decoding the user input 
def decrypt_reversed_base64(flag):
    try:
        # Decode the provided base64 string
        
        decoded_bytes = #base64.b64decode(flag)
        decoded_string = decoded_bytes.decode()

        return decoded_string
    except Exception as e:
        return f"Decryption failed: {e}"

if __name__ == "__main__":
    # Setting value for the flag variable
    flag = SUdOSVRFe0ZJUlNUQ09ERX0=

    # Perform decryption on the value supplied to the FLAG variable
    result = encrypt_reversed_base64(flag)

    # Display the decoded base64 string
    print("Decrypted Output:", result)