words = input().split()
dictionary = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1
for dict_key, dict_value in dictionary.items():
    if dict_value % 2 != 0:
        print(dict_key, end=" ")