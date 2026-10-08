#count words in sentence

def count_words(s):
  count=1
  for i in range(len(s)):
    if s[i]==" ":
      count=count+1
  return count
print(count_words("i love you neha"))
