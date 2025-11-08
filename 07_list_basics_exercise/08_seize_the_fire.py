level_of_fire = input().split("#")
water = int(input())
total_effort = 0
total_fire = 0
valid_cells = []

for fire in level_of_fire:
    fire_type_and_value = fire.split(" = ")
    fire_type, value_of_cell = fire_type_and_value[0], int(fire_type_and_value[1])
    is_valid = False

    if fire_type == "Low":
        if 1 <= value_of_cell <= 50:
            is_valid = True
    elif fire_type == "Medium":
        if 51 <= value_of_cell <= 80:
            is_valid = True
    elif fire_type == "High":
        if 81 <= value_of_cell <= 125:
            is_valid = True

    if is_valid:
        if water >= value_of_cell:
            water -= value_of_cell
            current_effort = value_of_cell * 0.25
            total_effort += current_effort
            total_fire += value_of_cell
            valid_cells.append(value_of_cell)

print("Cells:")
for cell in valid_cells:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")


