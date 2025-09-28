lst = input().split(' ')
faro_shuffles = int(input())
for _ in range(faro_shuffles):
    middle_of_the_deck = len(lst) // 2
    left = lst[:middle_of_the_deck]
    right = lst[middle_of_the_deck:]
    deck_after_shuffling = []
    for i in range(len(left)):
        deck_after_shuffling.append(left[i])
        deck_after_shuffling.append(right[i])
    lst = deck_after_shuffling.copy()
print(lst)