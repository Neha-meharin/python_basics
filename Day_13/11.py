# Take a number and a digit from the user.

# Count how many times that digit appears in the number.

# Example:

# Enter number: 552525
# Enter digit: 5

# 5 appears 4 times



n=552525
d=5
rev=0
count=0
while(n>0):
    rev=n%10
    if d==rev:
        count=count+1
    n=n//10
print(count) 
