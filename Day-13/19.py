s=input("entr")
count=""
for i in range(len(s)):
       count=s[i]+count
print(count)
if count==s:
       print("palindrome")
