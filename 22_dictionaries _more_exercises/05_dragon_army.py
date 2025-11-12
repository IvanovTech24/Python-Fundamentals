def parse_state(value: str, default: int) -> int:
    """Checks if the provided value is null.
       If null, returns the default value.
       Otherwise, converts it to an integer"""
    return int(value) if value != "null" else default

def read_dragons(some_n: int) -> dict:
    """Reads the information about the dragons.
        n -> number of data rows.
        Return a dictionary in the format
        {
            'Red': {
                'Bazgargal': {'damage': 100, 'health': 2500, 'armor': 25},
                'Obsidion': {'damage': 220, 'health': 2200, 'armor': 35}
            },
            'Blue': {
                'Kerizsa': {'damage': 60, 'health': 2100, 'armor':20}
            }
        }
        """
    some_dragons = {}
    for _ in range(some_n):
        dragon_type, name, damage, health, armor = input().split()
        damage = parse_state(damage, 45)
        health = parse_state(health, 250)
        armor = parse_state(armor, 10)
        # if the dragon type not in dictionary, add it.
        if dragon_type not in some_dragons:
            some_dragons[dragon_type] = {}
        # add or update the dragon with its new values.
        some_dragons[dragon_type][name] = {"damage": damage, "health": health, "armor": armor}
    return some_dragons

def calculate_average(some_dragons: dict) -> dict:
    """Calculate the average values (damage, health, armor) for each dragon type.
        Return a dictionary:
        {
            'Red': (160.00, 2350.00, 30.00),
            'Blue': (62.50, 1950.00, 35.00)
        }
        """
    some_average = {}
    for dragon_type, dragon_data in some_dragons.items():
        count = len(dragon_data)
        avg_damage = sum(d["damage"] for d in dragon_data.values()) / count
        avg_health = sum(d["health"] for d in dragon_data.values()) / count
        avg_armor = sum(d["armor"] for d in dragon_data.values()) / count

        some_average[dragon_type] = (avg_damage, avg_health, avg_armor)
    return some_average

def print_dragons(some_dragons: dict, averages: dict) -> None:
    """Print the results in the format:
        Type::(avg_damage/avg_health/avg_armor)
        -Name -> damage: x, health: y, armor: z"""
    for dragon_type, (avg_dmg, avg_hp, avg_arm) in averages.items():
        print(f"{dragon_type}::({avg_dmg:.2f}/{avg_hp:.2f}/{avg_arm:.2f})")\

        # Sort the dragon names in ascending order
        sorted_dragons = sorted(some_dragons[dragon_type].items())
        for name, stats in sorted_dragons:
            print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")

# Begins the program execution.
n = int(input())
dragons = read_dragons(n)
average = calculate_average(dragons)
print_dragons(dragons, average)






# n = int(input())
# dragons_dictionary = {}
# for _ in range(n):
#     dragon_types, dragon_name, damage, health, armor = input().split(" ")
#     if damage == "null":
#         damage = 45
#     if health == "null":
#         health = 250
#     if armor == "null":
#         armor = 10
#     damage = int(damage)
#     health = int(health)
#     armor = int(armor)
#     if dragon_types not in dragons_dictionary:
#         dragons_dictionary[dragon_types] = {}
#     dragons_dictionary[dragon_types][dragon_name] = {"damage": damage, "health": health, "armor": armor}
# for dragon_type, dragons in dragons_dictionary.items():
#     total_damage = 0
#     total_health = 0
#     total_armor = 0
#     for stats in dragons.values():
#         total_damage += stats["damage"]
#         total_health += stats["health"]
#         total_armor += stats["armor"]
#     count = len(dragons)
#     avg_damage = total_damage / count
#     avg_health = total_health / count
#     avg_armor = total_armor / count
#     print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
#
#     sorted_dragons = sorted(dragons.items())
#     for name, stats in sorted_dragons:
#         print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")

