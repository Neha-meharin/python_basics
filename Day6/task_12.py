inc=int(input("enter income"))
tax= 0
if inc<= 10000:
    tax= 0
elif inc <= 20000:
    x = inc - 10000
    tax= x * 10 / 100
else:
    tax= 0
    tax= 10000 * 10 / 100
    tax += (inc - 20000) * 20 / 100
print("Total tax to pay", tax)
