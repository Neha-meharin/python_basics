#making two list as a dictionary 

names = ["Neha", "Anu", "Rahul"]
marks = [75, 92, 68]

s={}
for i in range(len(names)) :
   name=names[i]
   mark=marks[i]
   s[names[i]]=marks[i]
print(s)
