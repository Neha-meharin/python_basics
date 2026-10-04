#factorial using function


def facto(a):
    fact = 1
    
    for i in range(1, a + 1):
        # update fact here
        fact=fact*i
    
    return fact
print(facto(3))
