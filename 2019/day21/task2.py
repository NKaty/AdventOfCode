from intcode import process_instructions


def get_hull_damage(data):
    start_message = ''
    end_message = ''
    instructions = """OR A J
    AND B J
    AND C J
    NOT J J
    AND D J
    NOT J T
    OR E T
    OR H T
    AND T J
    RUN
    """

    gen = process_instructions(data, [])

    while (output := next(gen)) != 10:
        start_message += chr(output)

    print(start_message)
    output = gen.send(list(map(ord, instructions)))

    while output is not None and output < 256:
        end_message += chr(output)
        output = next(gen)

    print(end_message)
    return output


if __name__ == "__main__":
    with open('day21/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(get_hull_damage(ns))  # 1140450681
