#Find the last character that appears only once.


s = "swiss"
p = {}

for i in s:
    if i not in p:
        p[i] = 1
    else:
        p[i] = p[i] + 1

print(p)
for i in range(len(s) - 1, -1, -1):
    if p[s[i]] == 1:
        print(s[i])
        break
        
