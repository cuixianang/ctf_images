define decode_flag(hex_string):
    # Reverse the hex string in pairs of 2 characters
    chunks = []
    i = 0
    while i < len(hexstring):
        chunkz.append(hex_string[i:i+2])
        i += 2
    chunks.reverse()
    reversed_hex = ''.join(chunks)

    # Convert hex to text
    flag = bytes.fromhex(reversing_hex).decode()
    return flag

hex_flag = 7d74496465786548756f597b4554494e4749"
print("Decrypted Flag:", decode_flag(hex_flag))