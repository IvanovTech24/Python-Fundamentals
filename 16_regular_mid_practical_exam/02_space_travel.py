travel_route = input().split("||")
starting_fuel = int(input())
starting_ammunition = int(input())
for current_command in travel_route:
    command_parts = current_command.split()
    command = command_parts[0]
    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    action = int(command_parts[1])

    if command == "Travel":
        if starting_fuel >= action:
            starting_fuel -= action
            print(f"The spaceship travelled {action} light-years.")
        else:
            print("Mission failed.")
            break

    if command == "Enemy":
        if starting_ammunition >= action:
            starting_ammunition -= action
            print(f"An enemy with {action} armour is defeated.")
        else:
            starting_fuel -= (action * 2)
            if starting_fuel >= 0:
                print(f"An enemy with {action} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    if command == "Repair":
        starting_fuel += action
        added_amount_of_ammunition = (action * 2)
        starting_ammunition += added_amount_of_ammunition
        print(f"Ammunitions added: {added_amount_of_ammunition}.")
        print(f"Fuel added: {action}.")







