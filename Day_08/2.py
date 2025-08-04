s = input("Enter a string: ")
half = (len(s) + 1) // 2  
new_string = s[half:] + s[:half]

print(new_string)
