list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    print("20 is present in the list")
    get = list1.index(20)
    print("The index of 20 is:", get)
    list1[get] = 200
    print("The updated list is:", list1)
