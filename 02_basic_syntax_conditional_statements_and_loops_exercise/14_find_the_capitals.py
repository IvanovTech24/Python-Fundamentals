word = input()
list_of_index = []
for index in range(len(word)):
    if word[index].isupper():
        list_of_index.append(index)
print(list_of_index)