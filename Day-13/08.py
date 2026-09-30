#check whether a number  is palindrome

n=121
p=n
reverse=0
while (n>0):
    reverse=reverse*10+(n%10)
    n=n//10
print(reverse)
if reverse==p:
    print("yey")
else:
    print("duh")
