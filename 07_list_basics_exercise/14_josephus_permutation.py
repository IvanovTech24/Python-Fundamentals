people_in_the_circle = [int(x) for x in input().split()]
number_to_kill = int(input())
index_to_remove = 0
killed_list = []

while len(people_in_the_circle) > 0:
    index_to_remove = (index_to_remove + number_to_kill - 1) % len(people_in_the_circle)
    killed_list.append(people_in_the_circle[index_to_remove])
    people_in_the_circle.pop(index_to_remove)

print("[", end="")
for index in range(len(killed_list)):
    print(killed_list[index], end="")
    if index != len(killed_list) - 1:
        print(",", end="")
print("]")
