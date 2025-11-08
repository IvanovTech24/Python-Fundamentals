money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integers = []
for money in money_as_string:
    money_as_integers.append(int(money))
beggars_sum = []
start_index = 0
for beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for index in range(start_index, len(money_as_integers), number_of_beggars):
        current_beggar_sum += money_as_integers[index]
    beggars_sum.append(current_beggar_sum)
    start_index += 1
print(beggars_sum)
