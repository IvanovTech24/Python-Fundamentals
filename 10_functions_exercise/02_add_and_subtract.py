# def sum_numbers(first_number, second_number):
#     result = first_number + second_number
#     return result
# def subtract(sum_of_numbers, third_number):
#     result = sum_of_numbers - third_number
#     return result
# def add_and_subtract(first_number, second_number, third_number):
#     sum_result = sum_numbers(first_number, second_number)
#     subtract_result = sum_result - third_number
#     return subtract_result
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# result_ = add_and_subtract(num1, num2, num3)
# print(result_)

#-----------------------solution I.Shopov-------------------
def sum_numbers(first: int, second: int) -> int:
    return first + second

def subtract(some_result: int, third: int) -> int:
    return some_result - third

def add_and_subtract(first_integer: int, second_integer: int, third_integer: int) -> int:
    returned_result = sum_numbers(first_integer, second_integer)
    final_result = subtract(returned_result, third_integer)
    return  final_result

first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)

























# def sum_numbers(first_number, second_number):
#     result = first_number + second_number
#     return result
#
# def subtract(result, third_number):
#     numbers_subtract = result - third_number
#     return numbers_subtract
#
# def add_and_subtract(first_number, second_number, third_number):
#     numbers_sum = sum_numbers(first_number, second_number)
#     numbers_subtract = subtract(numbers_sum, third_number)
#     return numbers_subtract
#
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# result_ = add_and_subtract(num1, num2, num3)
# print(result_)