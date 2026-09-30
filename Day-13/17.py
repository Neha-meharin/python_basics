#vowels
s=input("entr")
vowels=['a','e','i','o','u']
count=0
for i in range(len(s)):
       if  s[i] in vowels:
              count=count+1
print(count)
