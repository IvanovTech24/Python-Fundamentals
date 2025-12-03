import re

income = 0
while True:
    command = input()
    if command == "end of shift":
        break
    name = ""
    product = ""
    count = 0
    price = 0
    total_price = 0
    pattern = r"%([A-Z][a-z]+)%[^|%$.]*<(\w+)>[^|%$.]*\|([0-9]+)\|[^|%$.0-9]*([0-9]+(?:\.[0-9]+)?)\$"
    matches = re.findall(pattern, command)
    for match in matches:
        name += match[0]
        product += match[1]
        count += int(match[2])
        price += float(match[3])
    total_price = (count * price)
    if total_price != 0:
        print(f"{name}: {product} - {total_price:.2f}")
    else:
        continue
    income += total_price
print(f"Total income: {income:.2f}")