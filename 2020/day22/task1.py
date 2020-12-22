def find_score(decks):
    while decks[0] and decks[1]:
        card1 = decks[0].pop(0)
        card2 = decks[1].pop(0)
        if card1 > card2:
            decks[0] += [card1, card2]
        else:
            decks[1] += [card2, card1]

    winner = decks[0] or decks[1]
    return sum(card * count for card, count in zip(winner, range(len(winner), 0, -1)))


if __name__ == "__main__":
    with open('day22/input.txt') as inp:
        cards = [[int(card) for card in deck.strip().split('\n')[1:]] for deck in
                 inp.read().strip().split('\n\n')]

    print(find_score(cards))  # 32677
