from intcode import process_instructions


def process_computer_communication(data, computer_num, special_address):
    computers = [process_instructions(data[:], [i, -1]) for i in range(computer_num)]
    special_packet = None
    last_sent_special_packet = None

    while True:
        is_packet_sent = False
        for computer in computers:
            output = next(computer)
            if output is not None:
                is_packet_sent = True
                address, x, y = output
                if address == special_address:
                    special_packet = [x, y]
                    continue
                computers[address].send([x, y])

        if not is_packet_sent and special_packet:
            computers[0].send(special_packet)
            if last_sent_special_packet and last_sent_special_packet[1] == special_packet[1]:
                return special_packet[1]
            last_sent_special_packet = special_packet
            special_packet = None


if __name__ == "__main__":
    with open('day23/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(process_computer_communication(ns, 50, 255))  # 11504
