def reverse_engineer_handshake(key, value, subject_number, divider):
    loop_size = 0
    while True:
        value = value * subject_number % divider
        loop_size += 1
        if value == key:
            return loop_size


def find_encryption_key(public_keys, value, subject_number, divider):
    loop_size = reverse_engineer_handshake(public_keys[0], value, subject_number, divider)
    return pow(public_keys[1], loop_size, divider)


if __name__ == "__main__":
    with open('day25/input.txt') as inp:
        keys = [int(line.strip()) for line in inp]

    print(find_encryption_key(keys, 1, 7, 20201227))  # 9620012
