text = input()
text_lower = text.lower()
words = ["sand", "water", "fish", "sun"]
count = 0
for word in words:
    count += text_lower.count(word)
print(count)


