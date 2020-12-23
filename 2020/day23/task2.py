class Cup:
    def __init__(self, value, next_cup=None):
        self.value = value
        self.next = next_cup


class CupList:
    def __init__(self, items):
        self.dict = {}
        self.current = None
        self.create_circle(items)

    def create_circle(self, items):
        self.current = Cup(items[0])
        self.dict[items[0]] = self.current
        tail = self.current
        for item in items[1:]:
            tail.next = Cup(item)
            self.dict[item] = tail.next
            tail = tail.next
        tail.next = self.current

    @staticmethod
    def get_values(first, length):
        values = []
        current = first
        for _ in range(length):
            values.append(current.value)
            current = current.next
        return values


def play_game(cups, last, moves):
    cups = cups + list(range(max(cups) + 1, last + 1))
    cl = CupList(cups)

    for _ in range(moves):
        first_in_removed = cl.current.next
        cl.current.next = cl.current.next.next.next.next

        removed = cl.get_values(first_in_removed, 3)
        destination_value = cl.current.value - 1 or last
        while destination_value in removed:
            destination_value = destination_value - 1 or last

        destination_cup = cl.dict[destination_value]
        first_in_removed.next.next.next = destination_cup.next
        destination_cup.next = first_in_removed
        cl.current = cl.current.next

    return cl.dict[1].next.value * cl.dict[1].next.next.value


if __name__ == "__main__":
    with open('day23/input.txt') as inp:
        crab_cups = list(map(int, list(inp.read().strip())))

    print(play_game(crab_cups, 1000000, 10000000))  # 91408386135
