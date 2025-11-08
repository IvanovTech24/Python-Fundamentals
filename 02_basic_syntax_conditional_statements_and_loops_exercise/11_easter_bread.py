budget = float(input())
price_per_kilo_flour = float(input())

price_per_pack_of_egg = price_per_kilo_flour * 0.75
price_per_litter_of_milk = price_per_kilo_flour * 1.25
price_per_one_bread = price_per_kilo_flour + price_per_pack_of_egg + (price_per_litter_of_milk / 4)
number_of_loaves = 0
colored_eggs = 0
money_left = budget
while money_left >= price_per_one_bread:
    money_left -= price_per_one_bread
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")




