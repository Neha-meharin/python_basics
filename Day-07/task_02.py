def con(M):
    C = float((F - 32) *5/9)
    return f"temp is {round(C,1)}"
F=int(input("Enter temperature in Fahrenheit: "))
print(con(F))
