day=input("enter string")
count=0
for char in day:
    if  char.isdigit():
      count+=1
if count==0:
    print("type one num")
