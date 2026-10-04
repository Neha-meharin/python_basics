#convert tuple into list without using list()

numbers = (1, 2, 2, 3, 4, 2, 5, 2)
new=[]
for i in numbers:
    new.append(i)
print(new)
