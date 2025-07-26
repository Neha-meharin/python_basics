h=[10,30,20]
b=[]
for i in range(3):
    for g in range (i):
        b.append(h.pop(-1))
print(b)
    
