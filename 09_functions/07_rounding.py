def rounding(numbers_as_string: list):
    round_numbers = [round(float(num)) for num in numbers_as_string]
    # round_numbers = []
    # for num in numbers_as_string:
    #     round_numbers.append(round(float(num)))
    return round_numbers

numbers = input().split()
result = rounding(numbers)
print(result)