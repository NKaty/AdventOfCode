from intcode import process_instructions


def process_computer_communication(data, computer_num, special_address):
    computers = [process_instructions(data[:], [i, -1]) for i in range(computer_num)]
    while True:
        for computer in computers:
            output = next(computer)
            if output is not None:
                address, x, y = output
                if address == special_address:
                    return y
                computers[address].send([x, y])


if __name__ == "__main__":
    with open('day23/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(process_computer_communication(ns, 50, 255))  # 16660
