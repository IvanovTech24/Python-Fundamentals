def calculate_factorial(number: int) -> int:
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_factorial = calculate_factorial(first_number)
second_factorial = calculate_factorial(second_number)
print(f"{first_factorial / second_factorial:.2f}")
