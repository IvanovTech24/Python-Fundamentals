days_of_adventure = int(input())
number_of_participants = int(input())
total_group_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())



total_water = (number_of_participants * water_per_person_per_day) * days_of_adventure
total_food = (number_of_participants * food_per_person_per_day) * days_of_adventure

for day in range(1, days_of_adventure + 1):
    daily_energy_loss = float(input())
    total_group_energy -= daily_energy_loss
    if total_group_energy <= 0:
        break

    if day % 2 == 0:
        total_group_energy += total_group_energy * 0.05
        total_water -= total_water * 0.3
    if day % 3 == 0:
        total_group_energy += total_group_energy * 0.10
        total_food -= total_food / number_of_participants

if total_group_energy > 0:
    print(f"You are ready for the quest. You will be left with {total_group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")