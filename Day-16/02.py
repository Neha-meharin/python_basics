# Find the first non-repeating character

# Given:

# s = "swiss"

# Find the first character that appears only once.
n = "SWISS"
frequency={}

for i in range(len(n)):
 if n[i] in frequency:
       frequency[n[i]]=frequency[n[i]]+1
 else:
     frequency[n[i]]=1



for i in range(len(frequency)):
    if frequency[n[i]]==1:
        p=n[i]
        break
print(p)
       
 
