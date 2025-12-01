import re

encrypted_message = input()
pattern = r"([*^])([A-Za-z\s]{6,})([*^])([^A-Za-z0-9]*)([+]{1,})(-?[0-9]+\.[0-9]+)(,)(-?[0-9]+\.[0-9]+)([+]{1,})"
matches = re.finditer(pattern, encrypted_message)
artifact_name = []
coordinates = []

for match in matches:
    latitude = match.group(6)
    longitude = match.group(8)
    artifact_name.append(match.group(2))
    coordinates.append((latitude, longitude))

is_found = False
for name, current_coordinates in zip(artifact_name, coordinates):
    print(f"Found {name} at coordinates {current_coordinates[0]},{current_coordinates[1]}.")
    is_found = True
if not is_found:
    print("No valid artifacts found.")