def even(number):
    b = []
    for i in range(4, 30):
        if i % 2 == 0:
            b.append(i)
    return b

result = even(10)
print(result)
