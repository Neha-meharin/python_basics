wor=input("enter your password")
if len(wor)<8:
    print("pass too short")
flag=0
wordflag=0
for char in wor:
    if char.isupper()==True:
       wordflag=1
    if char.isdigit()==True:
        flag=1
if wordflag==1 and flag==1:
    print("word accepted")
else:
    print("word not accepted")
