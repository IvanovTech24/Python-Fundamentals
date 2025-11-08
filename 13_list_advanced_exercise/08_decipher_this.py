messages = input().split()
deciphered_message = []
for message in messages:
    message = list(message)
    numbers_as_string = ""
    for index in range(len(message)):
        if message[index].isdigit():
            numbers_as_string += message[index]
        else:
            break
    numbers_as_letter = chr(int(numbers_as_string))
    message = [numbers_as_letter] + message[index:]
    message[1], message[-1] = message[-1], message[1]
    deciphered_message.append("".join(message))
print(" ".join(deciphered_message))

