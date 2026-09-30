#frequency count of digits in dictionary 

n = [10, 0,25, 7, 42, 18,10,25,2,0]
frequency={}

for i in range(len(n)):
 if n[i] in frequency:
       frequency[n[i]]=frequency[n[i]]+1
 else:
     frequency[n[i]]=1

print(frequency)


