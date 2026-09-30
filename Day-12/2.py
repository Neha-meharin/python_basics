#Create a recursive function that returns the sum of numbers from 1 to n.
def count(n):
    if n<0:
        return 0
    return n + count(n-1)
e=count(5) 
print(e)
