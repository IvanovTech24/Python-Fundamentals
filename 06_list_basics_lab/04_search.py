num_of_lines = int(input())
magic_word = input()

my_list = []

for _ in range(num_of_lines):
    some_strings = input()
    my_list.append(some_strings)
print(my_list)

filtered_list = []

for current_string in my_list:
    if magic_word in current_string:
        filtered_list.append(current_string)
print(filtered_list)

