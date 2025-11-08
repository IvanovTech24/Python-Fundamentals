data = input().split()

stock = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i + 1])
    stock[key] = value

print(stock)