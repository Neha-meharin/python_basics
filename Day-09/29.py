n={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
s=input("enter digit")
d=[]
c=[]
for i in s:
    d.append(n[int(i)])
for i in range(len(d[0])):
    for j in range(len(d[1])):
        c.append(d[0][i]+d[1][j])
print(c)



