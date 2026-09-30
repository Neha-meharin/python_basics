sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

d = input("Enter key to Remove:")
if d in sample_dict:
    sample_dict.pop(d)
    print(sample_dict)
else:
    print("Key not found.")

