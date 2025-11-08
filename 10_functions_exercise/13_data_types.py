def integer(some_number: str) -> int:
    result = int(some_number) * 2
    return result

def real(some_number: str) -> float:
    result = float(some_number) * 1.5
    return result

def string(some_string: str) -> str:
    result = "$" + some_string + "$"
    return result



command_name = input()
number = input()

if command_name == "int":
    data_output = integer(number)
    print(data_output)
elif command_name == "real":
    data_output = real(number)
    print(f"{data_output:.2f}")
elif command_name == "string":
    data_output = string(number)
    print(data_output)

