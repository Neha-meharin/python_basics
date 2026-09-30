contacts = {
    "Ne": {
        "phone": "51234567",
        "email": "n@email.com",
        "address": "1fgh"
    },
    "Hvf": {
        "phone": "0987654",
        "email": "bft@email.com",
        "address": "oiuytre"
    }
}

def search(name):
    if name in contacts:
        contact = contacts[name]
        return f"\n{name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
    else:
        return f"\nContact '{name}' not found."

def edit(name):
    if name in contacts:
        phone = input("New Ph: ")
        email = input("New Em: ")
        address = input("New Add: ")
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        return f"\nContact for '{name}' updated."
    else:
        return f"\nContact '{name}' not found."

def disp():
    if not contacts:
        return "\nNo contacts available."
    sort = sorted(contacts.items())
    result = ""
    for name, info in sort:
        result += f"\n\n{name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}"
    return result

while True:
    print("\n===== Contact Book Menu =====")
    print("1. Search Contact")
    print("2. Edit Contact")
    print("3. Display All Contacts")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        name = input("Enter name to search: ").title()
        print(search(name))

    elif choice == "2":
        name = input("Enter name to edit: ").title()
        print(edit(name))

    elif choice == "3":
        print(disp())

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
