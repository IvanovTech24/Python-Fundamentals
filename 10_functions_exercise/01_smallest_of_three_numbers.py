# def smallest_number(first_number, second_number, third_number):
#     result = None
#     if (first_number <= second_number) and (first_number <= third_number):
#         result = first_number
#     elif (second_number <= first_number) and (second_number <= third_number):
#         result = second_number
#     else:
#         result = third_number
#     return result
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# result_ = smallest_number(num1, num2, num3)
# print(result_)

#--------------------solution I.Shopov---------------------
def find_smallest_number(numbers:list) -> int:
    return min(numbers)

first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = find_smallest_number([first_number, second_number, third_number])
print(smallest_number)


