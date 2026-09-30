words = ["apple", "ant", "banana", "bat", "cat", "cow"]
grouped = {}

for word in words:
    first=word[0]
    if first in grouped:
       grouped[first].append(word)
    else:
        grouped[first] = [word]
        
print(grouped)
