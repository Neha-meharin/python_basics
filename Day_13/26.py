# Move all zeros to the end

# Given:

# numbers = [0, 1, 0, 3, 12]

# Output:

# [1, 3, 12, 0, 0]

n = [10, 0,25, 7, 42, 18,10,25,2,0]
s=[]
count=0
for i in range(len(n)):
    if n[i]  !=0:
        s.append(n[i])
    else:
        count=count+1
for i in range(count):
    s.append(0)
print(s)
