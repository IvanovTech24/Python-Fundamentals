def loot(current_treasure_chest: list, current_items: list) -> list:
     for current_item in current_items:
         if current_item not in current_treasure_chest:
             current_treasure_chest.insert(0, current_item)
     return current_treasure_chest

def drop(current_treasure_chest: list, current_index: int) -> list:
    if current_index in range(len(current_treasure_chest)):
        removed_item = current_treasure_chest.pop(current_index)
        current_treasure_chest.append(removed_item)
    return current_treasure_chest

def steal(current_treasure_chest: list, current_count: int) -> list:
    if current_count >= len(current_treasure_chest):
        print(", ".join(current_treasure_chest))
        current_treasure_chest = []
    else:
        stealing_index = len(current_treasure_chest) - current_count
        print(", ".join(current_treasure_chest[stealing_index:]))
        current_treasure_chest = current_treasure_chest[:stealing_index]
    return current_treasure_chest

treasure_chest = input().split("|")
command = input().split()
while command[0] != "Yohoho!":
    action = command[0]
    if action == "Loot":
        items = command[1:]
        treasure_chest = loot(treasure_chest, items)
    elif action == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)
    elif action == "Steal":
        count = int(command[1])
        treasure_chest = steal(treasure_chest, count)
    command = input().split()

if not treasure_chest: # if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    # total_length = 0
    # for item in treasure_chest:
    #     total_length += len(item)
    # average_gain = total_length / len(treasure_chest)
    average_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")