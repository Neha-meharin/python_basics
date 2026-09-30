x = input("Enter string: ")
d = {}

for char in x:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

print(d)
