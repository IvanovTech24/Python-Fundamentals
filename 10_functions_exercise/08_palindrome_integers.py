def is_palindrome(some_number_as_string: str) -> bool:
    return some_number_as_string == some_number_as_string[::-1]

numbers = input().split(", ")
for number in numbers:
    print(is_palindrome(number))