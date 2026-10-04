#type of value is string or not 

student = {
    "name": "Neha",
    "age": 22,
    "marks": 85,
    "course": "Python"
}
count=0

for i,v in student.items():
    if type(v)==str:
        count=count+1
print(count)
