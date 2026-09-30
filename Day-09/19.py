word=input("Enter a word: ")
s=""
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        p=word[i:j]
        s+=p+" "
print("All possible substrings",s)
max=0
if word==word[::-1]:
    if len(word)>max:
        max=len(word)
        print("longest palindrome is",word)


