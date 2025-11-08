key = int(input())
number_of_lines = int(input())
decrypted_int = 0
decrypted_message = ""
for _ in range(number_of_lines):
    char = input()
    char_to_int = ord(char)
    decrypted_int = char_to_int + key
    int_to_char = chr(decrypted_int)
    decrypted_message += int_to_char
print(decrypted_message)
