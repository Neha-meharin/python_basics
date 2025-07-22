name = input("Enter string: ")
symb = "!@$%^&*()_+~"
name1 = ""

for char in name:
    if char in symb:
        name1 += "#"
    else:
        name1 += char

print("Modified string:", name1)
