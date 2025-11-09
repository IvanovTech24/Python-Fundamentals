materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
legendary_item = ""
won_a_legendary_item = False
while not won_a_legendary_item:
    current_item = input().split()
    for index in range(0, len(current_item), 2):
        key = current_item[index + 1].lower()
        value = int(current_item[index])
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value
        if materials["shards"] >= 250:
            materials["shards"] -= 250
            legendary_item = "Shadowmourne"
            won_a_legendary_item = True
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            legendary_item = "Valanyr"
            won_a_legendary_item = True
        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            legendary_item = "Dragonwrath"
            won_a_legendary_item = True
        if won_a_legendary_item:
            break
print(f"{legendary_item} obtained!")
for material, quantity in materials.items():
    print(f"{material}: {quantity}")







# materials = {
#     "shards": 0,
#     "fragments": 0,
#     "motes": 0
# }
# legendary_item = ""
# won_a_legendary_item = False
# while not won_a_legendary_item:
#     current_items = input().split()
#     for index in range(0, len(current_items), 2):
#         key = current_items[index + 1].lower()
#         value = int(current_items[index])
#         if key not in materials.keys():
#             materials[key] = 0
#         materials[key] += value
#         if materials["shards"] >= 250:
#             materials["shards"] -= 250
#             legendary_item = "Shadowmourne"
#             won_a_legendary_item = True
#         elif materials["fragments"] >= 250:
#             materials["fragments"] -= 250
#             legendary_item = "Valanyr"
#             won_a_legendary_item = True
#         elif materials["motes"] >= 250:
#             materials["motes"] -= 250
#             legendary_item = "Dragonwrath"
#             won_a_legendary_item = True
#         if won_a_legendary_item:
#             break
# print(f"{legendary_item} obtained!")
# for material, quantity in materials.items():
#     print(f"{material}: {quantity}")