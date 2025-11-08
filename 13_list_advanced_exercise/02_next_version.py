version = [int(digit) for digit in input().split(".")]
version[- 1] += 1
for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
print(".".join([str(digit) for digit in version]))

#------------------second solution-------------------
version = input().split(".")
version_as_integer = int("".join(version))
version_as_integer += 1
version_as_list = list(str(version_as_integer))
print(".".join(version_as_list))


