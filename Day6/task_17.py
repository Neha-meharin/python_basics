name=input("enter string")
chars=0
digits=0
symb=0

for char in name:

    if char.isdigit():
        digits+=1
        print(char)
        
    if char.isalpha():
        chars=chars+1
        print(char)
    else:
        symb+=1
charnum=chars
dignum=digits
symbnum=symb
print(charnum,dignum,symbnum)
