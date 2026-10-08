#how many digits in number

def count(int):
    count=0
    while int>0:
        int=int//10
        count=count+1
    return count
print(count(12345))
