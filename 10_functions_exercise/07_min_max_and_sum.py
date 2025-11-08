def min_number(some_numbers: list) -> int:
    some_minimum_number = min(some_numbers)
    return some_minimum_number

def max_number(some_numbers: list) -> int:
    some_maximum_number = max(some_numbers)
    return some_maximum_number

def sum_number(some_numbers: list) -> int:
    some_sum_number = sum(some_numbers)
    return some_sum_number


numbers = [int(x) for x in input().split()]

minimum_number = min_number(numbers)
maximum_number = max_number(numbers)
sum_of_numbers = sum_number(numbers)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_numbers}")
