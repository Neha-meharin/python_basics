#print common numbers in two list
n = [10, 25, 7, 42, 18,10,25,2]
l=[18,25]
s=[]
for i in range(len(n)):
    if n[i]  in l:
        s.append(n[i])
print(l)
