li1 = [1, 2, 3, 4, 5]
li2 = [4, 5, 6, 7, 8]

common = []
for item in li1:
    if item in li2 and item not in common:
        common.append(item)
print("Common elements:", common)
