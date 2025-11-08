def sorted_number(some_numbers: list) -> list:
    sorted_list = sorted(some_numbers)
    return sorted_list

numbers = [int(x) for x in input().split()]
result = sorted_number(numbers)
print(result)
