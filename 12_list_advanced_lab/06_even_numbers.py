numbers = list(map(int, input().split(", ")))
# even_index_number = []
# for index in range(len(numbers)):
#     if numbers[index] % 2 == 0:
#         even_index_number.append(index)
# print(even_index_number)

even_index_number = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

print(even_index_number)
