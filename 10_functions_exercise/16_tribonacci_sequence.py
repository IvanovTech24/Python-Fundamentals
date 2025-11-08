def tribonacci_sequence(number: int) -> list:
    first_three = [1, 1, 2]
    result = []
    if number <= 3:
        return first_three[:number]

    result = first_three.copy()
    for index in range(3, number):
        next_number = result[index - 1] + result[index - 2] + result[index - 3]
        result.append(next_number)
    return result


number_to_tribonacci = int(input())
result_as_string = tribonacci_sequence(number_to_tribonacci)
print(" ".join(map(str, result_as_string)))