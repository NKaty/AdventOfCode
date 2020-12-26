def find_duplicate_frequency(frequencies):
    seen = {0, }
    s = 0
    while True:
        for frequency in frequencies:
            s += frequency
            if s in seen:
                return s
            else:
                seen.add(s)


if __name__ == "__main__":
    with open('day01/input.txt') as inp:
        sequence = [int(line.strip()) for line in inp]

    print(find_duplicate_frequency(sequence))  # 71961
