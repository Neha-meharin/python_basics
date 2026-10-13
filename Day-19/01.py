s = "programming"
p = {}

for i in s:
    if i not in p:
        p[i] = 1
    else:
        p[i] = p[i] + 1

print(p)
for i in p:
    if p[i]==1:
        print(i)
        break
