manipulated_list = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        break

    #разделяме си частите на командата, така, че да ползваме всяка една от тях
    command_parts = command.split()
    #при команда-----------exchange----------------------------------------------------
    if command_parts[0] == "exchange":
        index = int(command_parts[1])
        if 0 <= index < len(manipulated_list):
            manipulated_list = manipulated_list[index + 1 :] + manipulated_list[: index + 1]
        else:
            print("Invalid index")

    # при команда----------------min/max-------------------------------------------
    elif command_parts[0] in ["min", "max"]:
        filtered_list = [] #създаваме си нов празен списък за всяка команда
        even_odd = command_parts[1]

        # филтрираме елементите---------------------------------------------
        for element in manipulated_list:
            if even_odd == "even" and element % 2 == 0:
                filtered_list.append(element)
            elif even_odd == "odd" and element % 2 != 0:
                filtered_list.append(element)

        # проверяваме дали има намерени елементи
        if not filtered_list:
            print("No matches")
        else:
            # намираме min-нималните и max-сималните стойности-----------------------------
            if command_parts[0] == "max":
                value = max(filtered_list)
            else:
                value = min(filtered_list)
            #търсим min или max стойност в оригиналният списък отзад-напред
            for index in range(len(manipulated_list)-1, -1, -1):
                if manipulated_list[index] == value:
                    print(index)
                    break
    #при команда------------------first/last--------------------------------
    elif command_parts[0] in ["first", "last"]:
        filtered_list = [] #отново създаваме нов празен списък за всяка команда
        count = int(command_parts[1])
        even_odd = command_parts[2]

        #проверяваме дали стойността в count е валидна т.е. е в диапазона на дължината на списъка
        if count > len(manipulated_list):
            print("Invalid count")
            continue

        #филтрираме елементите, за да намерим even/odd и да ги добавим във filtered_list
        for index in manipulated_list:
            if even_odd == "even" and  index % 2 == 0:
                filtered_list.append(index)
            elif even_odd == "odd" and index % 2 != 0:
                filtered_list.append(index)

        #вземаме първите или последните елементи
        if command_parts[0] == "first":
            result = filtered_list[:count]
        elif command_parts[0] == "last":
            #проверяваме count ако е по-малко от 0 да отпечатаме празен списък (според условието)
            if count > 0:
                result = filtered_list[-count:]
            else:
                result = []
        print(result)

print(manipulated_list)




