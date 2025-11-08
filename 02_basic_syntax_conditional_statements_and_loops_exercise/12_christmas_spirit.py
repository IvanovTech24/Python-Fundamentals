quantity_of_decorations = int(input())
remaining_days = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
spirit_ornament_set = 5
spirit_tree_skirt = 3
spirit_tree_garland = 10
spirit_tree_lights = 17

total_price = 0
total_spirit = 0
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_price += ornament_set_price * quantity_of_decorations
        total_spirit += spirit_ornament_set
    if current_day % 3 == 0:
        total_price += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += spirit_tree_skirt + spirit_tree_garland
    if current_day % 5 == 0:
        total_price += tree_lights_price * quantity_of_decorations
        total_spirit += spirit_tree_lights
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_price += tree_skirt_price + tree_garland_price + tree_lights_price
if remaining_days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")


