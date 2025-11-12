dwarf_data = {}
color_count = {}
while True:
    command = input()
    if command == "Once upon a time":
        break
    name, color, physics = command.split(" <:> ")
    physics = int(physics)
    key = name, color
    if key not in dwarf_data.keys():
        dwarf_data[key] = physics
    else:
        if dwarf_data[key] < physics:
            dwarf_data[key] = physics
for (name, color), physics in dwarf_data.items():
    if color not in color_count.keys():
        color_count[color] = 0
    color_count[color] += 1
sorted_dwarf = sorted(dwarf_data.items(), key=lambda x: (-x[1], -color_count[x[0][1]]))
for (name, color), physics in sorted_dwarf:
    print(f"({color}) {name} <-> {physics}")



# dwarf_data = {}
# color_count = {}
# while True:
#     command = input()
#     if command == "Once upon a time":
#         break
#     name, hat_color, physics = command.split(" <:> ")
#     physics = int(physics)
#     # create a key with two values
#     key = (name, hat_color)
#
#     if key not in dwarf_data.keys():
#         dwarf_data[key] = physics
#     else:
#         # keep the physics with higher value
#         if dwarf_data[key] < physics:
#             dwarf_data[key] = physics
# # keep track of different hat colors in color_count (dictionary)
# for (name, color), physics in dwarf_data.items():
#     if color not in color_count.keys():
#         color_count[color] = 0
#     color_count[color] += 1
# # sorting the data by points and color in descending order
# sorted_dwarf = sorted(dwarf_data.items(), key=lambda x: (-x[1], -color_count[x[0][1]]))
#
# for (name, color), physics in sorted_dwarf:
#     print(f"({color}) {name} <-> {physics}")