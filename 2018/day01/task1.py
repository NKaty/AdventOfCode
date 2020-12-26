def find_resulting_frequency(frequencies):
    return sum(frequencies)


if __name__ == "__main__":
    with open('day01/input.txt') as inp:
        sequence = [int(line.strip()) for line in inp]

    print(find_resulting_frequency(sequence))  # 502
