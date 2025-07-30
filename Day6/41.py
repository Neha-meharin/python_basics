my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))   
print(sorted_dict)
