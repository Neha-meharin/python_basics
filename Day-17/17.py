#print average of numbers


marks = {
    "Neha": 75,
    "Anu": 92,
    "Rahul": 68,
    "Akhil": 88
}
average=0
for i,v in marks.items():
    average=average+v

avg=average/len(marks)
print(avg)
    
