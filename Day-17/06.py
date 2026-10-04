#largest number in tuple

numbers = (10, 20, 30, 40, 50,60)
count=0
for i in numbers:
    if count<i:
      count=i
print(count)
