import re

bought_furniture = []
total_cost = 0
pattern = r">{2}([A-Za-z]+)<{2}(\d+\.?\d*)!(\d+)"
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        # furniture_name = match.groups(1)
        # price = match.groups(2)
        # quantity = match.groups(3)
        furniture_name, price, quantity = match.groups()
        bought_furniture.append(furniture_name)
        total_cost += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")