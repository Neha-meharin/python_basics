numbers = [10,5, 8, 2, 15, 2]
faloo=[]

for i in range(len(numbers)):
    if numbers[i] not in faloo:
        faloo.append(numbers[i])
print(faloo)
smallest=faloo[0]
second_smallest=faloo[0]


for i in range(len(faloo)):
   if faloo[i]>smallest:
       second_smallest=smallest
       smallest=faloo[i]
       


print(smallest)
print(second_smallest)

