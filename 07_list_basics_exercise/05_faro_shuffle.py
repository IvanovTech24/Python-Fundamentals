deck_of_cards = input().split()
numbers_of_shuffle = int(input())
for _ in range(numbers_of_shuffle):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[: middle_of_deck]
    right_part = deck_of_cards[middle_of_deck :]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_cards = deck_after_shuffling.copy()
print(deck_of_cards)


