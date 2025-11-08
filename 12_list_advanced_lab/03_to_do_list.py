to_do_list = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    current_command = command.split("-")
    index_priority = int(current_command[0]) - 1
    note = current_command[1]
    to_do_list.pop(index_priority)
    to_do_list.insert(index_priority, note)

result = [element for element in to_do_list if element != 0]
print(result)
