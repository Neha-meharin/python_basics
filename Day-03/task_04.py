import random
num=int(random.randint(1,10))
while True:
  g=int(input("enter num"))

  if g==num:
    print(f"you guessed it")
    break
  elif g<num:
    print(f"too low")
  else :
    print(f"too high")
