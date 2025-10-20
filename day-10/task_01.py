n=input("enter your thought")
with open("notes.txt", "w") as file:
    file.write(n)
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)  
print("success")
