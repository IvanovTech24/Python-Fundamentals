import re

sentence = input()
searched_word = input()
pattern = fr"(?i)\b{searched_word}\b"
matches = re.findall(pattern, sentence)
# matches = re.findall(patter, sentence, re.IGNORCASE)
print(len(matches))