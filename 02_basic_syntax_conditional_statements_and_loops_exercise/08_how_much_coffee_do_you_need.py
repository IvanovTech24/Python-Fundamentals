number_of_coffee = 0
extra_coffee_needed = 5
while True:
    command = input()
    if command == "END":
        break
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        number_of_coffee += 1
    if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        number_of_coffee += 2
if number_of_coffee > extra_coffee_needed:
    print("You need extra sleep")
else:
    print(number_of_coffee)


