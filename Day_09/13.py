num = input("Enter a number: ")   # keep as string
res = 0
for digit in num:
    res = res + int(digit)        # convert each char back to int
print("Sum of digits:", res)
