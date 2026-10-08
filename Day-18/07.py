def lar(n):
     large=n[0]
     for i in range(len(n)):
          if large<n[i]:
               large=n[i]
     return large
print(lar([10, 5, 8, 20, 3]))



