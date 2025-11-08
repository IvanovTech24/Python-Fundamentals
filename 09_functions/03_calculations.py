def calculates(operator: str, first_number: int, second_number: int):
    result = None
    if operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number
    elif operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number // second_number
    return result

operator_ = input()
first_number_ = int(input())
second_number_ = int(input())
result_ = calculates(operator_, first_number_, second_number_)
print(result_)