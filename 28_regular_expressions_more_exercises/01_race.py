import re

names = input().split(", ")
participants = {}
while True:
    total_km = 0
    command = input()
    if command == "end of race":
        break
    pattern_for_letter = r"[a-z]+"
    pattern_for_digits = r"\d"
    match_name = re.findall(pattern_for_letter, command, re.IGNORECASE)
    match_digits = re.findall(pattern_for_digits, command)
    current_name = "".join(match_name)
    distance = [int(km) for km in match_digits]
    for km in distance:
        total_km += km
    if current_name in names:
        if current_name not in participants.keys():
            participants[current_name] = 0
        participants[current_name] += total_km
sorted_participants = sorted(participants.items(), key=lambda x: x[1], reverse=True)
top_three = sorted_participants[:3]
print(f"1st place: {top_three[0][0]}")
print(f"2nd place: {top_three[1][0]}")
print(f"3rd place: {top_three[2][0]}")