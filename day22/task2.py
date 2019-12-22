import re


def deal_into_new_stack(inc, offset, deck_len):
    inc = inc * -1 % deck_len
    offset = (offset + inc) % deck_len
    return inc, offset


def cut(inc, offset, deck_len, num):
    offset = (offset + inc * num) % deck_len
    return inc, offset


def deal_with_increment(inc, offset, deck_len, num):
    inc *= pow(num, deck_len - 2, deck_len)
    return inc, offset


def shuffle_cards(techs, cards_number, times, card_index):
    shuffle_dict = {
        'deal into new stack': deal_into_new_stack,
        'deal with increment': deal_with_increment,
        'cut': cut}

    inc, offset = 1, 0
    for tech, arg in techs:
        arg = (arg,) if arg is not None else tuple()
        args = (inc, offset, cards_number) + arg
        inc, offset = shuffle_dict[tech](*args)

    final_inc = pow(inc, times, cards_number)
    final_offset = offset * (1 - final_inc) * pow(1 - inc, cards_number - 2, cards_number)

    return (final_offset + card_index * final_inc) % cards_number


if __name__ == "__main__":
    techniques = []
    with open('day22/input.txt') as inp:
        for line in inp:
            arg = re.search(r'-?\d+', line)
            techniques.append((re.sub(r'-?\d+', '', line).strip(), int(arg.group(0)) if arg is not None else arg))

    print(shuffle_cards(techniques, 119315717514047, 101741582076661, 2020))  # 63967243502561
