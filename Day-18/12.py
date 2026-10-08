#
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i]+numbers[j]==6:
         print(numbers[i],numbers[j])
