number_of_line = int(input())
tank_capacity = 255
for _ in range(number_of_line):
    liters_of_water = int(input())
    if liters_of_water > tank_capacity:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water
print(255 - tank_capacity)
