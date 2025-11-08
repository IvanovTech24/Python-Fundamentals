def multiply_sign(some_first_number: int, some_second_number: int, some_third_number: int) -> str:
    result = ""
    if some_first_number == 0 or some_second_number == 0 or some_third_number == 0:
        result = "zero"
        return result

    negative_count = 0
    if some_first_number < 0:
        negative_count += 1
    if some_second_number < 0:
        negative_count += 1
    if some_third_number < 0:
        negative_count += 1

    if negative_count % 2 == 0:
        result = "positive"
        return result
    else:
        result = "negative"
        return result

first_number = int(input())
second_number = int(input())
third_number = int(input())
multiplication_result = multiply_sign(first_number, second_number, third_number)
print(multiplication_result)
