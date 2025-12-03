import re

n = int(input())
attacked_planet = []
destroyed_planet = []
for _ in range(n):
    letters = ""
    count = 0
    decrypted_message = ""
    message = input()
    for letter in message:
        letter = letter.lower()
        if letter == "s" or letter == "t" or letter == "a" or letter == "r":
            letters += letter
    count += len(letters)
    for letter in message:
        letter = ord(letter)
        letter -= count
        new_letter = chr(letter)
        decrypted_message += new_letter
    pattern = r"@([A-Z][a-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!(A|D)![^@\-!:>]*->(\d+)"
    matches = re.findall(pattern, decrypted_message)
    for match in matches:
        planet_name = match[0]
        population = int(match[1])
        attack_type = match[2]
        soldier_count = int(match[3])
        if attack_type == "A":
            attacked_planet.append(planet_name)
        elif attack_type == "D":
            destroyed_planet.append(planet_name)
        if not matches:
            continue
attacked_planet = sorted(attacked_planet)
destroyed_planet = sorted(destroyed_planet)
print(f"Attacked planets: {len(attacked_planet)}")
if attacked_planet:
    for planet in attacked_planet:
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planet)}")
if destroyed_planet:
    for planet in destroyed_planet:
        print(f"-> {planet}")