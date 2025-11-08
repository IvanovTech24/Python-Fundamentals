numbers_as_string = input().split()
remove_counter = int(input())
numbers_as_integers = []
for element in numbers_as_string:
    numbers_as_integers.append(int(element))
for _ in range(remove_counter):
    min_number = min(numbers_as_integers)
    numbers_as_integers.remove(min_number)
print(", ".join(map(str, numbers_as_integers)))
