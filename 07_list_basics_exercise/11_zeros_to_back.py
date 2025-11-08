numbers_list = [int(x) for x in input().split(", ")]
new_number_list = []
zero_counter = []
for element in numbers_list:
    if element == 0:
        zero_counter.append(element)
    else:
        new_number_list.append(element)

for number in zero_counter:
    new_number_list.append(number)

print(new_number_list)


