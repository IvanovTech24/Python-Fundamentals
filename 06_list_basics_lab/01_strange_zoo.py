first_string = input()
second_string = input()
third_string = input()

my_list = [first_string, second_string, third_string]

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)
