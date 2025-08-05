def hi(a):
    r = {}
    for item in a:
        r[item] = r.get(item, 0) + 1

    result = [item for item in r if r[item] == 1]
    print(result)

list1 = [1, 2, 3, 2, 4]
hi(list1)
