numbers_list = [int(x) for x in input().split()]
message = input()
message_list = []
for number in numbers_list:
    sum_of_numbers = 0
    number_as_string = str(number)
    for element in number_as_string:
        number_as_integer = int(element)
        sum_of_numbers += number_as_integer
    if sum_of_numbers < len(message):
        index_to_remove = sum_of_numbers
    else:
        index_to_remove = sum_of_numbers % len(message)
    message_list.append(message[index_to_remove])
    new_message = message[: index_to_remove] + message[index_to_remove + 1 :]
    message = new_message

print("".join(message_list))












