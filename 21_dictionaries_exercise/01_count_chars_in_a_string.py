characters = input()
letters = {}
for char in characters:
    if char == " ":
        continue
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1
for character, occurrences in letters.items():
    print(f"{character} -> {occurrences}")