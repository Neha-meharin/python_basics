#Find the student with the highest mark

marks = {
    "Neha": 75,
    "Anu": 92,
    "Rahul": 68,
    "Akhil": 88
}
largest=0
mae=""
for i,v in marks.items():
    if largest<v:
        largest=marks[i]
        mae=i
print(largest)
print(mae)
