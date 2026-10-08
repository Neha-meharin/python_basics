#palindrome function

def reverse(str):
    h=""
    for i in range(len(str)):
        h=str[i]+h
    if str==h:
        return True
print(reverse("madam"))
