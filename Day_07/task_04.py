def add(a,b):
    res=a+b
    return res
def sub(a,b):
    res=a-b
    return res
def mul(a,b):
    res=a*b
    return res

while True:
        print("-----menu------")
        print("1.add")
        print("2.sub")
        print("3.mul")
        print("4.Exit")
        opt=int(input("enter one option"))
        if opt==1:
            n=int(input("enter first num"))
            m=int(input("enter second num"))
            print(add(n,m))
        elif opt==2:
            n=int(input("enter first num"))
            m=int(input("enter second num"))
            print(sub(n,m))
        elif opt==3:
            n=int(input("enter first num"))
            m=int(input("enter second num"))
            print(mul(n,m))
        elif opt == "4":
            print("Exiting the program.")
            break
      
