#from collections import defaultdict
from zmq.backend import first

# counts = defaultdict(int)
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# for word in words:
#     counts[word] += 1
# print(counts)

#---------------------------Dictionary Comprehension--------------------
first_list = ["Ivan", "Simo", "Petko"]
second_list = [15, 25, 35]
# my_dictionary = {}
# for index in range(len(fist_list)):
#     my_dictionary[fist_list[index]] = second_list[index]
# print(my_dictionary)
# my_dictionary = {name: ages for (name, ages) in zip(fist_list, second_list)}
# print(my_dictionary)

zipped_dict = zip(first_list, second_list)
# print(dict(zipped_dict))

# for name, age in zip(first_list, second_list):
#     print(f"{name} is {age} years old")

#----------------------------Итерираране пре ключове--------------------------
my_dictionary = {"Ivan": 24, "Milen": 15, "Stoyan": 33}
# for key in my_dictionary.keys():
#     my_dictionary[key] = 1
# print(my_dictionary)

#--------------------------------Итериране през стойности---------------------------
for value in my_dictionary.values():
    print(value, end="  ")
