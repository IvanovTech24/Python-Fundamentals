some_string = input()
final_string = ""
sub_string = ""
repetitions = ""
for index in range(len(some_string)):
    # Case where we have non-numeric symbol
    if not some_string[index].isdigit():
        sub_string += some_string[index]
    # Case where we have digit
    else:
        repetitions += some_string[index]
        if index + 1 < len(some_string):
            if some_string[index + 1].isdigit():
                repetitions += some_string[index + 1]
        final_string += int(repetitions) * sub_string.upper()
        sub_string = ""
        repetitions = ""
count_unique_symbol = len(set(final_string))
print(f"Unique symbols used: {count_unique_symbol}")
print(final_string)