
import random
print("1.6-side")
print("2.20-side")
print("3. multiple")
choice = int(input("Enter choice"))
if choice == 1:
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}")
elif choice == 2:
    roll = random.randint(1, 20)
    print(f"You rolled a {roll}")
elif choice == 3:
    sides = int(input("Enter num of side "))
    num = int(input("no.of dice "))
    for i in range(num):
        print(f"Dice {i+1}: {random.randint(1, sides)}")
else:
    print("nop")
