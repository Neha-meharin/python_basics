# Write a Python program that takes a number and calculates the sum of all its digits.

n=121
count=0
while(n>0):
    count=count+n%10
    n=n//10
    
print(count)
