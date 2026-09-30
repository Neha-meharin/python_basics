# Write a Python program that takes a number and counts how many digits it has.

# Examples:

# Enter a number: 12345
# Number of digits: 5

n=121
count=0
while(n>0):
    n=n//10
    count=count+1
print(count)
