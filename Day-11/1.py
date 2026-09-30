try:
    num1 = float(input("Enter num1"))
    num2 = float(input("Enter num2"))
    if num2 == 0:
        print("Error:")
        result = None
    else:
        result = num1 / num2
        with open("results.txt", "a") as file:
            file.write(f"{num1} / {num2} = {result}\n")
        print("Result:", result)
        print("Saved")
except ValueError:
    print("Error: Please enter valid numbers!")
