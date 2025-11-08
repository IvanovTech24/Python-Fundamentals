sequence_of_target = [int(x) for x in input().split()]
command = input().split()
while command[0] != "End":
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        if index in range(len(sequence_of_target)):
            sequence_of_target[index] -= value
            if sequence_of_target[index] <= 0:
                del sequence_of_target[index]
    elif action == "Add":
        if index in range(len(sequence_of_target)):
            sequence_of_target.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if (index - value not in range(len(sequence_of_target)) or
                index + value not in range(len(sequence_of_target))):
            print("Strike missed!")
        else:
            before_strike = sequence_of_target[:index - value]
            after_strike = sequence_of_target[index + value + 1:]
            sequence_of_target = before_strike + after_strike
    command = input().split()
print(*sequence_of_target, sep= "|")
# print("|".join(map(str, sequence_of_target)))
# print("|".join([str(x) for x in sequence_of_target]))
