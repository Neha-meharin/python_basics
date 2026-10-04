# print count of subject which have mark greater than 50

marks = {
    "math": 75,
    "english": 45,
    "science": 82,
    "history": 39,
    "computer": 91
}
count=0
for i,v in marks.items():
    if v>50:
        count=count+1 
print(count)
