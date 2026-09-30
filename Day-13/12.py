n=23326
larg=0
rev=0
while(n>0):
    rev=n%10
    if rev>larg:
        larg=rev
    n=n//10
print(larg) 
