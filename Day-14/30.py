sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

d = input("Enter key to extract: ")
if d in sample_dict:
    f = {d: sample_dict[d]}
    print(f)
else:
    print("Key not found.")

