import re

demons_name = [name.strip() for name in input().split(",")]
demons_name = sorted(demons_name)

for name in demons_name:
    pattern_health = r"[^0-9+\-*\/.]"
    matches_chars = re.findall(pattern_health, name)
    health = sum(ord(char) for char in matches_chars)

    pattern_numbers = r"[+-]?(?:\d+\.\d+|\d+)"
    matches_numbers = re.findall(pattern_numbers, name)
    damage = sum(float(number) for number in matches_numbers)

    pattern_operators = r"[*\/]"
    matches_operators = re.findall(pattern_operators, name)
    for operators in matches_operators:
        if operators == "*":
            damage *= 2
        elif operators == "/":
            damage /= 2
    print(f"{name} - {health} health, {damage:.2f} damage")