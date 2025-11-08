number_of_electrons = int(input())
shells = []
number_of_shells = 0
while number_of_electrons > 0:
    number_of_shells += 1
    max_electrons_in_current_shell = 2 * number_of_shells ** 2
    if number_of_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
    else:
        shells.append(number_of_electrons)
    number_of_electrons -= max_electrons_in_current_shell

print(shells)