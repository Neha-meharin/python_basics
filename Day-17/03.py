#Rotate a list to the right by one position


numbers = [1, 2, 3, 4, 5]
new=[]
new.append(numbers[len(numbers)-1])
for i in range(len(numbers)-1):
   new.append(numbers[i])
print(new)
