def rec(l,b):
  area=l*b
  pm=2*(l+b)
  return f"area is {area} and perimeter is {pm}"
le=int(input("length of rect"))
br=int(input("breadth of rect"))
print(rec(le,br))
