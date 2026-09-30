a=[]
b=[]
n1=int(input("Enter the number of elements in first list: "))
n2=int(input("Enter the number of elements in second list: "))

for i in range(0,n1):
    ele=int(input("Enter the element: "))
    a.append(ele)
for j in range(0,n2):
    w=int(input("Enter the element: "))
    b.append(w)

c=[]
merge=a+b
c=list(set(merge))
print("The merged list is: ",c)
h=len(c)
if h%2==0:
    mid=(c[h//2]+c[(h//2+1)])/2
else:
     mid=(c[h//2])+1
print("The median is: ",mid)
