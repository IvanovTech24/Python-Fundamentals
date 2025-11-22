# import itertools
# key = [int(number) for number in input().split()]
# while True:
#     decrypted_message = ""
#     encrypted_message = input()
#     if encrypted_message == "find":
#         break
#     for char, key_offset in zip(encrypted_message, itertools.cycle(key)):
#         decrypted_char = ord(char) - key_offset
#         decrypted_message += chr(decrypted_char)
#     type_start_index = decrypted_message.find("&") + 1
#     type_end_index = decrypted_message.find("&", type_start_index)
#     current_type = decrypted_message[type_start_index:type_end_index]
#     coordinate_start_index = decrypted_message.find("<") + 1
#     coordinate_end_index = decrypted_message.find(">")
#     coordinates = decrypted_message[coordinate_start_index:coordinate_end_index]
#     print(f"Found {current_type} at {coordinates}")

# Another solution without itertools:
key = [int(numbers) for numbers in input().split()]
while True:
    decrypted_message = ""
    index = 0
    encrypted_message = input()
    if encrypted_message == "find":
        break
    for char in encrypted_message:
        key_offset = key[index]
        index += 1
        if index == len(key):
            index = 0
        decrypted_char = ord(char) - key_offset
        decrypted_message += chr(decrypted_char)
    start_index_type = decrypted_message.find("&") + 1
    end_index_type = decrypted_message.find("&", start_index_type)
    current_type = decrypted_message[start_index_type:end_index_type]
    start_index_coordinate = decrypted_message.find("<") + 1
    end_index_coordinate = decrypted_message.find(">")
    coordinates = decrypted_message[start_index_coordinate:end_index_coordinate]
    print(f"Found {current_type} at {coordinates}")