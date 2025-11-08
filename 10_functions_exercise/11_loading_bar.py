def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percents = some_number // 10
    not_loaded_percent = 10 - loaded_percents
    return f"{some_number}% [{'%' * loaded_percents}{'.' * not_loaded_percent}] \nStill loading..."


number = int(input())
print(loading_bar(number))
