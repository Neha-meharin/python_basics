

while True:
    filename = input("Enter filenm ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content:" + content)
            break 
    except FileNotFoundError:
        print("Error")
