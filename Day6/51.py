num1 = str(9876543210)
largest_num=0
size = len(str(num1))
for i in range(size):
    if int(num1[i]) > largest_num:
        largest_num = int(num1[i])  
print("Largest digit in the number is:", largest_num)

