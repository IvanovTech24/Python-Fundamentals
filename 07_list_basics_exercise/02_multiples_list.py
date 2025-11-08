factor = int(input())
count = int(input())
numbers = []
for multiples in range(1, count + 1):
    numbers.append(factor * multiples)
print(numbers)