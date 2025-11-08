def merge(some_list: list, current_command: list) -> list:
    start_index, end_index = int(current_command[1]), int(current_command[2])
    if start_index not in range(len(some_list)):
        start_index = 0
    if end_index not in range(len(some_list)):
        end_index = len(some_list) - 1
    some_list[start_index] = "".join(some_list[start_index: end_index + 1])
    some_list = some_list[:start_index + 1] + some_list[end_index + 1:]
    return some_list

def divide(some_list: list, current_command: list) -> list:
    index, partitions = int(current_command[1]), int(current_command[2])
    element = some_list[index]
    partition_size = len(element) // partitions
    partitioned_elements = []
    number_of_partition = 0
    for current_index in range(0, len(element), partition_size):
        number_of_partition += 1
        if number_of_partition == partitions:
            current_partition = element[current_index:]
            partitioned_elements.append(current_partition)
            break
        else:
            current_partition = element[current_index: current_index + partition_size]
            partitioned_elements.append(current_partition)
    some_list = some_list[:index] + partitioned_elements + some_list[index + 1:]
    return some_list

initial_string_as_list = input().split()
command = input()

while command != "3:1":
    command = command.split()
    action = command[0]
    if action == "merge":
        initial_string_as_list = merge(initial_string_as_list, command)
    elif action == "divide":
        initial_string_as_list = divide(initial_string_as_list, command)
    command = input()
print(" ".join(initial_string_as_list))