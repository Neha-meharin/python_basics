s=int(input("enter number"))
b=bin(s)[2:]
c=""
for char in b:  
    if char=="1":
        e=char.replace("1","0")
        c=c+e
    else:
        e=char.replace("0","1")
        c=c+e
print(c)
f=int(c,2)
print(f)
