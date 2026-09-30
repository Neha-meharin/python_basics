fruit={'apple': 5, 'banana': 3}
print("old ist",fruit)
y=input("enter new fruit name")
v=input("enter value")
newfruit={}
newfruit=fruit.copy()
newfruit[y]=v
print("new list",newfruit)
u=input("which one to update")
b=input("value to update")
if u in newfruit:
    newfruit[u]=b
    print("updated list",newfruit)
