password = input()

while True:
    command = input()
    if command == "Complete":
        break
    command = command.split()
    action = command[0]
    if action == "Make":
        current_action = command[1]
        index = int(command[2])
        if current_action == "Upper":
            symbol = password[index]
            symbol = symbol.upper()
            before_index = password[:index]
            after_index = password[index + 1:]
            password = before_index + symbol + after_index
            print(password)
        elif current_action == "Lower":
            symbol = password[index]
            symbol = symbol.lower()
            before_index = password[:index]
            after_index = password[index + 1:]
            password = before_index + symbol + after_index
            print(password)
    elif action == "Insert":
        index = int(command[1])
        char = command[2]
        if 0 <= index <= len(password):
            before_index = password[:index]
            after_index = password[index:]
            password = before_index + char + after_index
            print(password)
    elif action == "Replace":
        char = command[1]
        value = int(command[2])
        if char not in password:
            continue
        char_to_ascii = ord(char)
        value += char_to_ascii
        new_char = chr(value)
        password = password.replace(char, new_char)
        print(password)
    elif action == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        for char in password:
            if not char.isdigit() and not char.isalpha() and char != "_":
                print("Password must consist only of letters, digits and _!")
                break

        is_found_upper = False
        for char in password:
            if char.isupper():
                is_found_upper = True
                break
        if not is_found_upper:
            print("Password must consist at least one uppercase letter!")

        is_found_lower = False
        for char in password:
            if char.islower():
                is_found_lower = True
                break
        if not is_found_lower:
            print("Password must consist at least one lowercase letter!")

        is_found_digit = False
        for char in password:
            if char.isdigit():
                is_found_digit = True
                break
        if not is_found_digit:
            print("Password must consist at least one digit!")

# Solution with functions
def make_upper(password: str, current_index: int) -> str:
    symbol = password[current_index]
    symbol = symbol.upper()
    before_index = password[:current_index]
    after_index = password[current_index + 1:]
    password = before_index + symbol + after_index
    print(password)
    return password


def make_lower(password: str, current_index: int) -> str:
    symbol = password[current_index]
    symbol = symbol.lower()
    before_index = password[:current_index]
    after_index = password[current_index + 1:]
    password = before_index + symbol + after_index
    print(password)
    return password


def insert_char(password: str, current_index: int, char: str) -> str:
    if 0 <= current_index <= len(password):
        before_index = password[:current_index]
        after_index = password[current_index:]
        password = before_index + char + after_index
        print(password)
    return password


def replace_char(password: str, char: str, value: int) -> str:
    char_to_ascii = ord(char)
    value += char_to_ascii
    new_char = chr(value)
    password = password.replace(char, new_char)
    print(password)
    return password


def validation_email(password: str) -> None:
    if len(password) < 8:
        print("Password must be at least 8 characters long!")

    for char in password:
        if not char.isdigit() and not char.isalpha() and char != "_":
            print("Password must consist only of letters, digits and _!")
            break

    is_found_upper = False
    for char in password:
        if char.isupper():
            is_found_upper = True
            break
    if not is_found_upper:
        print("Password must consist at least one uppercase letter!")

    is_found_lower = False
    for char in password:
        if char.islower():
            is_found_lower = True
            break
    if not is_found_lower:
        print("Password must consist at least one lowercase letter!")

    is_found_digit = False
    for char in password:
        if char.isdigit():
            is_found_digit = True
            break
    if not is_found_digit:
        print("Password must consist at least one digit!")


def main_function():
    password = input()

    while True:
        command = input()
        if command == "Complete":
            break
        command = command.split()
        action = command[0]
        if action == "Make":
            current_action = command[1]
            current_index = int(command[2])
            if current_action == "Upper":
                password = make_upper(password, current_index)
            elif current_action == "Lower":
                password = make_lower(password, current_index)
        elif action == "Insert":
            current_index = int(command[1])
            char = command[2]
            password = insert_char(password, current_index, char)
        elif action == "Replace":
            char = command[1]
            value = int(command[2])
            if char not in password:
                continue
            password = replace_char(password, char, value)
        elif action == "Validation":
            validation_email(password)
main_function()