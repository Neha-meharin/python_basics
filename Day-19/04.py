#Find the indices of two numbers whose sum equals target.

numbers = [3, 2, 4, 7, 5]
target = 9

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
         if numbers[i]+numbers[j]==target:
              print(numbers[i],numbers[j])
