items=["egg","water"]
newitem=input("enter new item you want to add")
items.append(newitem)
print("new list after adding item",items)
removeditem=input("enter  item you want to remove")
items.remove(removeditem)
print("new list after removed item",items)

print("to check if item is in list")

s=input("enter the item to search")
if items.count(s)>0:
  print("item exist  in the list")
else:
  print("item notexist  in the list")
