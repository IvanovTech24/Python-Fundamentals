# Solution with dictionary comprehension
# countries = input().split(", ")
# capitals = input().split(", ")
# dictionary = {countries[index]: capitals[index] for index in range(len(countries))}
# for country, capital in dictionary.items():
#     print(f"{country} -> {capital}")

# Solution with dictionary comprehension with zip()
countries = input().split(", ")
capitals = input().split(", ")
dictionary = {key: value for (key, value) in zip(countries, capitals)}
for country, capital in dictionary.items():
    print(f"{country} -> {capital}")

# Solution only with zip()
# countries = input().split(", ")
# capitals = input().split(", ")
# dictionary = dict(zip(countries, capitals))
# for country, capital in dictionary.items():
#     print(f"{country} -> {capital}")