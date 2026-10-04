#count vowels in string using function

def vowel(str):
    vowels={"a","e","i","o","u"}
    count=0
    for i in range(len(str)):
        if str[i] in vowels:
            count=count+1
    return count
print(vowel("hey neha"))
