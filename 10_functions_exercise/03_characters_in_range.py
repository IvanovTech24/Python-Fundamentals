def all_the_symbols(first: str, second: str) -> list:
    collected_symbols = []
    for current_symbol_as_integer in range(ord(first) + 1, ord(second)):
        collected_symbols.append(chr(current_symbol_as_integer))
    return collected_symbols


first_character = input()
second_character = input()
symbols = all_the_symbols(first_character, second_character)
print(" ".join(symbols))
