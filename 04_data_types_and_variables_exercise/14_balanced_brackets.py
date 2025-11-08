number_of_lines = int(input())
counter = 0
for _ in range(number_of_lines):
    current_string = input()
    if current_string == "(":
        counter += 1
    elif current_string == ")":
        counter -= 1
    else:
        continue
    if (counter > 1) or (counter < 0):
        break
if counter == 0:
    print("BALANCED")
else:
    print("UNBALANCED")