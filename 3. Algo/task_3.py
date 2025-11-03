import random

def quick_sort_deck(deck):
    if len(deck) < 4:
        return sorted(deck)
    if len(deck) >= 4:
        pivot = random.choice(deck)
        left_part = []
        right_part = []
        for i in deck:
            if i <= pivot:
                left_part.append(i)
        for i in deck:
            if i > pivot:
                right_part.append(i)
    return sorted(left_part) + sorted(right_part)

print(quick_sort_deck([7, 3, 3, 4, 1, 2, 5]))