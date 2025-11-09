number_of_commands = int(input())
parking = {}
for _ in range(number_of_commands):
    current_command = input().split()
    action = current_command[0]
    if action == "register":
        username, license_plate_number = current_command[1], current_command[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif action == "unregister":
        username = current_command[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")
for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")