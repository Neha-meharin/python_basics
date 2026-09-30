largest number in list
n = [10, 25, 7, 42, 18]
largest=n[0]
for i in range(len(n)):
 if n[i]>largest:
     largest=n[i]
print(largest)
