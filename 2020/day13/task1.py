import re
import math


def find_earliest_bus(departure, buses):
    wait = min([{'time': bus * math.ceil(departure / bus) - departure, 'id': bus} for bus in buses],
               key=lambda x: x['time'])
    return wait['time'] * wait['id']


if __name__ == "__main__":
    with open('day13/input.txt') as inp:
        lines = inp.readlines()
    departure_timestamp = int(lines[0].strip())
    schedule = [int(item) for item in re.findall(r'(\d+)', lines[1])]

    print(find_earliest_bus(departure_timestamp, schedule))  # 171
