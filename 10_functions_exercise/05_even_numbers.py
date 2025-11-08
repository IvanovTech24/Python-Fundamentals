# def is_even(numbers: int) -> bool:
#     return numbers % 2 == 0
#
#
# numbers_as_string = input().split()
# numbers_as_digits = []
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))
#     result = list(filter(is_even, numbers_as_digits))
# print(result)

#-----------------------solution without filter()-----------------------------------
# def is_even(number: int) -> bool:
#     return number % 2 == 0
#
# numbers_as_string = input().split()
# result = []
# for current_number in numbers_as_string:
#     if is_even(int(current_number)): #това  е еквивалент на: if is_even == True:
#         result.append(int(current_number))
# print(result)

#-------------------------solution with list comprehension-----------------------
print([int(number) for number in input().split() if int(number) % 2 == 0])
