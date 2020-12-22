def play_game(decks):
    seen = set()
    winner = None
    while decks[0] and decks[1]:
        winner = None
        decks_state = tuple(decks[0]), tuple(decks[1])
        if decks_state in seen:
            return 1, decks[0]
        seen.add(decks_state)

        card1 = decks[0].pop(0)
        card2 = decks[1].pop(0)

        if len(decks[0]) >= card1 and len(decks[1]) >= card2:
            deck1 = decks[0][:card1]
            deck2 = decks[1][:card2]
            winner, _ = play_game([deck1, deck2])

        if winner == 1 or (winner is None and card1 > card2):
            winner = 1
            decks[0] += [card1, card2]
        else:
            winner = 2
            decks[1] += [card2, card1]

    return winner, decks[0] or decks[1]


def find_score(decks):
    _, winner = play_game(decks)
    return sum(card * count for card, count in zip(winner, range(len(winner), 0, -1)))


if __name__ == "__main__":
    with open('day22/input.txt') as inp:
        cards = [[int(card) for card in deck.strip().split('\n')[1:]] for deck in
                 inp.read().strip().split('\n\n')]

    print(find_score(cards))  # 33661
