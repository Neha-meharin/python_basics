b=["a","a","b","c"]
e=[]
count=0
size=len(b)
print(size)
for i in range(size):
    if b[i] in e:
        count+=1
    else:
        e.append(b[i])
        count=1
print(e)
