#smallest in list

def fndsmall(n):
    small=n[0]
    for i in range(len(n)):
        if n[i]<small:
            small=n[i]
    return small
print(fndsmall([10, 5, 8, 2, 15]))
