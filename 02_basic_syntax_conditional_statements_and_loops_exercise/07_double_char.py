while True:
    current_string = input()
    if current_string == "End":
        break
    if current_string == "SoftUni":
        continue
    new_string = ""
    for index in range(len(current_string)):
        new_string += current_string[index] * 2
    print(new_string)

