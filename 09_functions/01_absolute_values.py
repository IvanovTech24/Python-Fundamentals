number_list = [float(x) for x in input().split()]

abs_value = []

for num in number_list:
    abs_value.append(abs(num))

print(abs_value)

#------------------solution with list comprehension ---------------------
# number_list = [float(x) for x in input().split()]
# abs_value = [abs(num) for num in number_list]
# print(abs_value)