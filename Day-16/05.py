numbers = [-5, 3, -2, 8, 0, -1, 7]
positive=[]
Negative=[]

for i in range(len(numbers)):
 if 0<numbers[i]:
   positive.append(numbers[i])
 elif 0>numbers[i]:
    Negative.append(numbers[i])

print("Positive:",positive)
print("Negative:",Negative)
