time_to_pass = [int(x) for x in input().split()]
total_time_left = 0
total_time_right = 0
finish_line = len(time_to_pass) // 2
left = time_to_pass[: finish_line]
right = time_to_pass[finish_line + 1 :]#[::-1]
right.reverse()
for index in left:
    if index == 0:
        total_time_left -= total_time_left * 0.2
        continue
    total_time_left += index
for index in right:
    if index == 0:
        total_time_right -= total_time_right * 0.2
        continue
    total_time_right += index
if total_time_left < total_time_right:
    print(f"The winner is left with total time: {total_time_left:.1f}")
else:
    print(f"The winner is right with total time: {total_time_right:.1f}")









