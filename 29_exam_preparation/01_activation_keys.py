def contains(some_activation_key: str, some_command: list) -> str:
    substring = some_command[1]
    if substring in some_activation_key:
        return f"{some_activation_key} contains {substring}"
    return "Substring not found!"

def flip(some_activation_key: str, some_command: list) -> str:
    upper_lower = some_command[1]
    start_index = int(some_command[2])
    end_index = int(some_command[3])
    before_substring = some_activation_key[:start_index]
    after_substring = some_activation_key[end_index:]
    substring = some_activation_key[start_index:end_index]
    if upper_lower == "Upper":
        substring = substring.upper()
    elif upper_lower == "Lower":
        substring = substring.lower()
    some_activation_key = before_substring + substring + after_substring
    return some_activation_key

def slice(some_activation_key: str, some_command: list) -> str:
    start_index = int(some_command[1])
    end_index = int(some_command[2])
    before_deleting = some_activation_key[:start_index]
    after_deleting = some_activation_key[end_index:]
    some_activation_key = before_deleting + after_deleting
    return some_activation_key


activation_key = input()
command = input()
while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        print(contains(activation_key, command))
    elif action == "Flip":
        activation_key = flip(activation_key, command)
        print(activation_key)
    elif action == "Slice":
        activation_key = slice(activation_key, command)
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")