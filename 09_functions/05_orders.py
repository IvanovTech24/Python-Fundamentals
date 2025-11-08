def calculate_orders(product: str, quantity: int):
    price = None
    if product == "coffee":
        price = 1.50 * quantity
    elif product == "coke":
        price = 1.40 * quantity
    elif product == "water":
        price = 1.00 * quantity
    elif product == "snacks":
        price = 2.00 * quantity
    return price

product_input = input()
quantity_ = int(input())
result = calculate_orders(product_input, quantity_)
print(f"{result:.2f}")