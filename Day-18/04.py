#add the sum of digits

def sum(n):
    count=0
    while n>0:
        s=n%10
        count=count+s
        n=n//10
    return count
print(sum(12345))
