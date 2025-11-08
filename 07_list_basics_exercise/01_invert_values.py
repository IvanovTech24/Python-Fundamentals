numbers = input().split()
opposite_numbers = []
for current_number in numbers:
    opposite_number = -int(current_number)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)