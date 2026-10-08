#second largest number in list

def lar(n):
     large=n[0]
     second=0
     for i in range(len(n)):
          if large<n[i]:
               second=large
               large=n[i]
               
     return second
print(lar([10, 5,8, 20,30, 3]))



