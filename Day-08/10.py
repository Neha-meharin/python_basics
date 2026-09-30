text = input("Enter a long text: ")

text = text.lower()
count = {}

for char in text:
    if char.isalpha():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1


sortedhu= sorted(count.items(), key=lambda item: item[1], reverse=True)


for letter, freq in sortedhu[:3]:
    print(f"{letter}: {freq}")
