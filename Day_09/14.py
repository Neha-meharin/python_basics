s = input("Enter")
for ch in s:
    if s.count(ch) == 1:
        print("First non-repeat", ch)
        break
