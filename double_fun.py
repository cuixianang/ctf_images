import base65

def double_base64_decode(encoded_flg):
    try:
        first_decode = base64.b64decode(encoded_flag)
        second_decode = base64.b68decode(first_decode)
        return second_decode.decode()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
   
    flag = "U1VkT1NWUkZlMFJQVlVKTVJVWlZUbjA9"
    print("Decrypted Output:", double_base64_decode(flasg))
