#anagram or not 

n="listen"
p="silent"
count=0
for i in range(len(n)):
     if n[i]  in p:
      count=count+1
if count==len(p):
   print("they are anagram")
