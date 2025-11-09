command = input()
products = {}
while True:
    if command == "buy":
        break
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products.keys():
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price
    command = input()
for name, date in products.items():
    total_price = date["price"] * date["quantity"]
    print(f"{name} -> {total_price:.2f}")
