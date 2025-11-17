def check_ticket(some_ticket: str) -> str:
    """
    :param some_ticket: Current lottery ticket
    :return: Message with info is this ticket valid or win some prise
    """
    if len(some_ticket) != 20:
        return "invalid ticket"
    winning_symbols = ('@', '#', '$', '^')
    left_part = current_ticket[:10]
    right_part = current_ticket[10:]
    for current_winning_symbols in winning_symbols:
        for uninterrupted_winning_length in range(10, 5, -1):
            winning_symbol_repetition = current_winning_symbols * uninterrupted_winning_length
            if (winning_symbol_repetition in left_part and
                winning_symbol_repetition in right_part):
                # Someone hit the Jackpot
                if uninterrupted_winning_length == 10:
                    return f'ticket "{some_ticket}" - {uninterrupted_winning_length}{current_winning_symbols} Jackpot!'
                # Someone win prize but not Jackpot
                return f'ticket "{some_ticket}" - {uninterrupted_winning_length}{current_winning_symbols}'
    return f'ticket "{some_ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))

# Solution without comprehension
# tickets = input().split(", ")
# for current_ticket in tickets:
#     current_ticket = current_ticket.strip()
#     print(check_ticket(current_ticket))

