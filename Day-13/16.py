#perfect number
n=8
sum=0
for i in range(1,n):
    if n%i==0:
       sum=sum+i
if sum==n:
       print("yes")
else:
     print("no")
