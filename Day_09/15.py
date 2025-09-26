r=int(input("enter no of rats"))
unit=int(input("enter unit"))
n=int(input('house no'))
a=[]

for i in range(n):
    b=int(input("enter food in house"))
    a.append(b)

sum=0
count=0
for i in range(n):
     sum=sum+a[i]
     count=count+1
     if sum>=r*unit:
        break     
print("no of houses that can be fed",count)   
if sum<r*unit:
    print("insufficient food")
