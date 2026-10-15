#append zeroes to the last of list without using new list

numbers = [0, 3, 0, 1, 5, 0, 2]
j=0

for i in range(len(numbers)):
      if numbers[i] != 0:
        numbers[j]=numbers[i]
        j=j+1
while j < len(numbers):
    numbers[j] = 0
    j =j+1 1

print(numbers)
