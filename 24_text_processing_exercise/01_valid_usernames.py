def length_is_valid(some_name: str) -> bool:
    if not 3 < len(some_name) < 16:
        return False
    return True

def symbol_are_valid(some_name: str) -> bool:
    for symbol in some_name:
        if not (symbol.isalnum() or symbol == "-" or symbol == "_"):
            return False
    return True

def no_redundant_symbol(some_name: str) -> bool:
    """

    :param some_name: Current username
    :return: True if (описваме при какво условиея), else: (описваме при какво условия)
    """
    if " " in some_name:
        return False
    return True

def name_is_valid(some_name: str) -> bool:
    if length_is_valid(some_name) and symbol_are_valid(some_name) and no_redundant_symbol(some_name):
        return True
    return False


usernames = input().split(", ")
for name in usernames:
    if name_is_valid(name):
        print(name)


# Another solution
usernames = input().split(", ")
for name in usernames:
    is_valid = True
    if not 3 < len(name) < 16:
        is_valid = False
    for symbol in name:
        if not (symbol.isalnum() or symbol == "-" or symbol == "_"):
            is_valid = False
    if " " in name:
        is_valid = False
    if is_valid:
        print(name)