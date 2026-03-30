def secret_function():
    return ''.join([chr(c) for c in [73, 71, 78, 73, 84, 69, 123, 89, 79, 85, 70, 79, 85, 78, 68, 77, 69, 125])

if __name__ == "__main__":
    result = secret_funtion()
    print("Writing to output.txt...")
    with open("output.txt", "w) as f:
        f.write(result) 
    print("Done.")