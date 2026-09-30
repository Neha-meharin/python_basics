n = int(input("Enter no of monkeys: "))
k = int(input("Enter no of peanuts eaten by a monkey: "))
j = int(input("Enter no of bananas eaten by a monkey: "))
m = int(input("Enter no of peanuts offered by people: "))
p = int(input("Enter no of bananas offered by people: "))
if k == 0 or j == 0:
    print("Invalid input (k or j cannot be zero)")
else:
    
    pe = m // k

    ba = p // j

    monleft = pe+ba

    remaining = n - monleft
    if remaining < 0:
        remaining = 0   
    print("Total no of monkeys remaining in tree is", remaining)
