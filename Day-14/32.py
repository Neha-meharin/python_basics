x=input("Enter string: ")
b=int(input("enter no.of characters removed: "))
for i in range(0,b):
    x=x.replace(x[0],"",b)
print(x)
