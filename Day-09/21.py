f=[1,2,3,4,5,6,7,8,9,10]
b=[]
c=[]

for digit in f:
    if digit%2==0:
        b.append(digit)
    if digit%2!=0:
        c.append(digit)
print(b)
print(c)
