collection_of_items = input().split("|")
budget = float(input())
ticket_price = 150
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50
current_expenses = 0
item_with_profit = 0
increase_budget = 0
selling_price_list = []

for element in collection_of_items:
    item_type_value = element.split("->")
    current_item, current_price = item_type_value[0], float(item_type_value[1])
    if budget < current_price:
        continue
    if current_item == "Clothes" and current_price <= clothes_max_price:
        budget -= current_price
        current_expenses += current_price
        item_with_profit = current_price + current_price * 0.4
        increase_budget += item_with_profit
        selling_price_list.append(f"{item_with_profit:.2f}")
    elif current_item == "Shoes" and current_price <= shoes_max_price:
        budget -= current_price
        current_expenses += current_price
        item_with_profit = current_price + current_price * 0.4
        increase_budget += item_with_profit
        selling_price_list.append(f"{item_with_profit:.2f}")
    elif current_item == "Accessories" and current_price <= accessories_max_price:
        budget -= current_price
        current_expenses += current_price
        item_with_profit = current_price + current_price * 0.4
        increase_budget += item_with_profit
        selling_price_list.append(f"{item_with_profit:.2f}")

print(" ".join(selling_price_list))
profit = increase_budget - current_expenses
print(f"Profit: {profit:.2f}")
budget += increase_budget
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")








