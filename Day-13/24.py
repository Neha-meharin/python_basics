#duplicate in list

n = [10, 25, 7, 42, 18,10,25,2]
l=[]
for i in range(len(n)):
    if n[i] not in l:
        l.append(n[i])

print(l)
