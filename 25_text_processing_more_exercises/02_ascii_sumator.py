first_char = ord(input())
second_char = ord(input())
random_string = input()
total_sum = 0
for char in random_string:
    char = ord(char)
    if first_char < char < second_char:
        total_sum += char
print(total_sum)