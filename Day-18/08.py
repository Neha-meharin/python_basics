#remove duplicates
def lar(n):
     d=[]
     for i in range(len(n)):
          if n[i] not in d:
               d.append(n[i])
     return d
print(lar([10, 5, 5,8, 20, 3]))



