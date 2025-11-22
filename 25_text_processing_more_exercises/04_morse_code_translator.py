def decode_morse(some_word: str) -> str:
    english_words = ""
    if some_word == ".-":
        english_words = "A"
    elif some_word == "-...":
        english_words = "B"
    elif some_word == "-.-.":
        english_words = "C"
    elif some_word == "-..":
        english_words = "D"
    elif some_word == ".":
        english_words = "E"
    elif some_word == "..-.":
        english_words = "F"
    elif some_word == "--.":
        english_words = "G"
    elif some_word == "....":
        english_words = "H"
    elif some_word == "..":
        english_words = "I"
    elif some_word == ".---":
        english_words = "J"
    elif some_word == "-.-":
        english_words = "K"
    elif some_word == ".-..":
        english_words = "L"
    elif some_word == "--":
        english_words = "M"
    elif some_word == "-.":
        english_words = "N"
    elif some_word == "---":
        english_words = "O"
    elif some_word == ".--.":
        english_words = "P"
    elif some_word == "--.-":
        english_words = "Q"
    elif some_word == ".-.":
        english_words = "R"
    elif some_word == "...":
        english_words = "S"
    elif some_word == "-":
        english_words = "T"
    elif some_word == "..-":
        english_words = "U"
    elif some_word == "...-":
        english_words = "V"
    elif some_word == ".--":
        english_words = "W"
    elif some_word == "-..-":
        english_words = "X"
    elif some_word == "-.--":
        english_words = "Y"
    elif some_word == "--..":
        english_words = "Z"
    return english_words

# morse_code = input().split(" | ")
# word_list = []
# for words in morse_code:
#     current_word = ""
#     words = words.split()
#     for letter in words:
#         current_word += decode_morse(letter)
#     word_list.append(current_word)
# print(" ".join(word_list))

more_code = input().split(" | ")
words_list = []
for words in more_code:
    current_word = ""
    words = words.split()
    for letter in words:
        current_word += decode_morse(letter)
    words_list.append(current_word)
print(" ".join(words_list))