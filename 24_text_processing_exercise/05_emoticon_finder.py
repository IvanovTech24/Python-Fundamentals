some_string = input()
for index in range(len(some_string)):
    if some_string[index] == ":":
        if index + 1 < len(some_string):
            print(f"{some_string[index]}{some_string[index + 1]}")