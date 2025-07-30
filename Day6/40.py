original_dict1 = {'a': 1, 'b': 2, 'c': 3}
o=len(original_dict1)

key = list(original_dict1.keys())
value = list(original_dict1.values())
new_dict1 = {}


for i in range(o):
    new_dict1[value[i]] = key[i] 
print(new_dict1)   

    
