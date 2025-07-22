name=input("enter name")
size=len(name)
m=int(size/2)
s=name[m]
n=name[m-1]
l=name[m+1]
res=n+s+l
print(res)
