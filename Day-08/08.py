paragraph = input("Enter a paragraph: ")

words = paragraph.split()

count= {}

for word in words:
    
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

frequent = max(count, key=count.get)

print("Most frequent word:", frequent)
print("Frequency:", count[frequent])
