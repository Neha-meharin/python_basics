#remove  char at positions where index % 3 == 0 

N = input("Enter word: ")
result = ""

for index in range(len(N)):
    if index % 3 != 0:
        result += N[index]

print(result)
