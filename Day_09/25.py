n=input("enter no of integers needed in list")
l=[]
for i in range(int(n)):
    a=int(input("enter integer"))
    l.append(a)
print(l)
count=0
for i in range(1,len(l)):
    if l[i-1]>l[i]:
       count=count+1
print(count+1)
