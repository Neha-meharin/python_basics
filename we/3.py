def cer(contact):
    name = input("Enter name")
    number = input("Enter num ")
    contact[name] = number
    with open("contact.txt", "a") as file:
        file.write(f"{name}:{number}\n")
    print("Cont saved")
def poi():
    with open("contact.txt", "r") as file:
        o = file.read()
        print("Contacts:" + o)
def search():
    name = input("Enter searchnme")
    found = False
    with open("contact.txt", "r") as file:
        for line in file:
            n, num = line.strip().split(":")
            if n == name:
                print(f"{n}: {num}")
                found = True
                break
    if not found:
        print("nop")
contact = {}
s = int(input("Choose one option:\n1. Add\n2. View\n3. Search\n"))

if s == 1:
    cer(contact)
elif s == 2:
    poi()
elif s == 3:
    search()
else:
    print("Invalid")
