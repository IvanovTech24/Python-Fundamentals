pairs_of_words = input().split(" | ")
test_words = input().split(" | ")
command = input()
my_dictionary = {}
for pair in pairs_of_words:
    word, definition = pair.split(": ")
    if word not in my_dictionary:
        my_dictionary[word] = []
    my_dictionary[word].append(definition)
if command == "Test":
    for test_word in test_words:
        if test_word in my_dictionary.keys():
            print(f"{test_word}:")
            for some_definition in my_dictionary[test_word]:
                print(f" -{some_definition}")
elif command == "Hand Over":
    print(" ".join(my_dictionary.keys()))