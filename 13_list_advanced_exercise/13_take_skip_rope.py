hidden_message = list(input())
numbers_list = []
string_list = []
take_list = []
skip_list = []
result = []
start_index = 0
for element in hidden_message:
    if element.isdigit():
        numbers_list.append(int(element))
    else:
        string_list.append(element)
take_list = numbers_list[0::2]
skip_list = numbers_list[1::2]
for index in range(len(take_list)):
    take_count = take_list[index]
    skip_count = skip_list[index]
    end_index = start_index + take_count
    if end_index > len(string_list):
        end_index = len(string_list)
    result.extend(string_list[start_index:end_index])
    start_index = end_index + skip_count
    if start_index >= len(string_list):
        break
print("".join(result))






