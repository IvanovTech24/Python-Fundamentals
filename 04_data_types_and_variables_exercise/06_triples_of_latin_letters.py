number_of_letter = int(input())
start_letter = 97

for first_char in range(start_letter, start_letter + number_of_letter):
    for second_char in range(start_letter, start_letter + number_of_letter):
        for third_char in range(start_letter, start_letter + number_of_letter):
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}")