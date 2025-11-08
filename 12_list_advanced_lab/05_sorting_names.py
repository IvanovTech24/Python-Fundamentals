names = input().split(", ")


def sorted_key(name: list) -> tuple:
    return (-len(name), name[0])

sorted_names = sorted(names, key=sorted_key)
print(sorted_names)

#-----------------------solution with lambda expression------------------
# sorted_names = sorted(names, key=lambda x: (-len(x), x))
# print(sorted_names)

#----------------------solution with function--------------------------
# def sorted_key(name):
#     return (-len(name), name[0])
#
# sorted_names = sorted(names, key=sorted_key)
# print(sorted_names)

#-----------------------solution with lambda expression------------------
# sorted_names = sorted(names, key=lambda x: (-len(x), x))
# print(sorted_names)
