import re


def deal_into_new_stack(deck):
    return deck[::-1]


def cut(deck, num):
    return deck[num:] + deck[:num]


def deal_with_increment(deck, num):
    deck_len = len(deck)
    new_deck = [None] * deck_len
    for i in range(deck_len):
        new_deck[i * num % deck_len] = deck[i]
    return new_deck


def shuffle_cards(techs, cards_number):
    shuffle_dict = {
        'deal into new stack': deal_into_new_stack,
        'deal with increment': deal_with_increment,
        'cut': cut}

    deck = list(range(cards_number))
    for tech, arg in techs:
        args = (deck, arg) if arg is not None else (deck,)
        deck = shuffle_dict[tech](*args)

    return deck


if __name__ == "__main__":
    techniques = []
    with open('day22/input.txt') as inp:
        for line in inp:
            arg = re.search(r'-?\d+', line)
            techniques.append((re.sub(r'-?\d+', '', line).strip(), int(arg.group(0)) if arg is not None else arg))

    print(shuffle_cards(techniques, 10007).index(2019))  # 2558
