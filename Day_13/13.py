# Take a number from the user and find the largest digit in that number.

# Example:

# Enter number: 58329

# Largest digit: 9

# Another:

# Enter number: 4217

# Largest digit: 7

n=23326
larg=0
rev=0
while(n>0):
    rev=n%10
    if rev>larg:
        larg=rev
    n=n//10
print(larg) 
