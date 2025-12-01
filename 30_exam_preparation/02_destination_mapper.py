import re

map_string = input()
pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, map_string)
destinations = [match[1] for match in matches]
# This represents list-comprehension
# destinations = []
# for match in matches:
#     destinations.append(match[1])
travel_points = sum(len(destination) for destination in destinations)
# This represents sum()
# travel_points = 0
# for destination in destinations:
#     travel_points += len(destination)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")


# # Solution with re.finditer()
matches = re.finditer(pattern, map_string)
destinations = [match.group(2) for match in matches]
# This represents list-comprehension
# for match in matches:
#     print(match.group(2))
travel_points = sum(len(destination) for destination in destinations)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")