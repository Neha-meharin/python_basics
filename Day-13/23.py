#reversing list
n = [10, 25, 7, 42, 18]
l=[]
for i in range(len(n)-1,0,-1):
 l.append(n[i])
print(l)
