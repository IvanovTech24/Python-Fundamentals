names_of_the_gifts = input().split()
names_of_the_gifts_list = []
for element in names_of_the_gifts:
    names_of_the_gifts_list.append(element)
gifts = names_of_the_gifts_list
while True:
    command = input().split()
    command_as_list = []
    for element in command:
        command_as_list.append(element)
    if command_as_list[0] == "OutOfStock":
        if command_as_list[1] in gifts:
            for current_gift in range(len(gifts)):
                if gifts[current_gift] == command_as_list[1]:
                    gifts[current_gift] = "None"
    elif command_as_list[0] == "Required":
        index_to_replace = int(command_as_list[2])
        if 0 <= index_to_replace < len(gifts):
            gifts[index_to_replace] = command_as_list[1]
    elif command_as_list[0] == "JustInCase":
        word_to_replace = command_as_list[1]
        gifts[-1] = word_to_replace
    command_to_break = (" ".join(map(str, command_as_list)))
    if command_to_break == "No Money":
        break
final_gifts = []
for element in gifts:
    if element != "None":
        final_gifts.append(element)
print(" ".join(final_gifts))