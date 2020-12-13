def find_earliest_timestamp(buses):
    timestamp = 0
    interval = buses[0][0]
    i = 1
    while i < len(buses):
        for bus in buses[i:]:
            if (timestamp + bus[1]) % bus[0] != 0:
                break
            interval *= bus[0]
            i += 1
        timestamp += interval
    return timestamp - interval


if __name__ == "__main__":
    with open('day13/input.txt') as inp:
        lines = inp.readlines()
    schedule = list(filter(lambda x: x[0] != 'x', map(lambda x: (int(x[1]), x[0]) if x[1] != 'x'
                    else (x[1], x[0]), enumerate(lines[1].strip().split(',')))))

    print(find_earliest_timestamp(schedule))  # 539746751134958
