#remove duplicate char

n="programming"
s=""
for i in range(len(n)):
     if n[i] not in s:
      s=s+n[i]
print(s)
