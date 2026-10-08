#reverse string using function

def reverse(str):
    h=" "
    for i in range(len(str)):
        h=str[i]+h
    return h
print(reverse("hello"))
