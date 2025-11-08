number = int(input())
counter = 0
if number <= 1:
    print("False")
else:
    for current_number in range(2, number):
        if number % current_number == 0:
            counter += 1
    if counter > 0:
        print("False")
    else:
        print("True")