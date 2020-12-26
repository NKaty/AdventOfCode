from collections import Counter


def count_checksum(ids):
    count2 = 0
    count3 = 0
    ids_counters = [Counter(Counter(_id).values()) for _id in ids]
    for counter in ids_counters:
        count2 += 1 if 2 in counter else 0
        count3 += 1 if 3 in counter else 0
    return count2 * count3


if __name__ == "__main__":
    with open('day02/input.txt') as inp:
        box_ids = [line.strip() for line in inp]

    print(count_checksum(box_ids))  # 6225
