population = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())

sum_of_all_population = sum(population)
sum_of_minimum_income_amount = minimum_wealth * len(population)

if sum_of_all_population < sum_of_minimum_income_amount:
    print("No equal distribution possible")
else:
    is_possible = True

    for index in range(len(population)):
        if population[index] < minimum_wealth:
            needed = minimum_wealth - population[index]
            richest_index = population.index(max(population))
            if population[richest_index] - needed >= minimum_wealth:
                population[index] += needed
                population[richest_index] -= needed
            else:
                is_possible = False
                break
    if is_possible:
        print(population)
    else:
        print("No equal distribution possible")


