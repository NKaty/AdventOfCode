from itertools import combinations


def find_similar_box_ids(ids):
    all_variants = set()
    for _id in ids:
        variants = set(''.join(item) for item in combinations(_id, len(_id) - 1))
        intersection = all_variants & variants
        if intersection:
            return intersection.pop()
        all_variants |= variants


if __name__ == "__main__":
    with open('day02/input.txt') as inp:
        box_ids = [line.strip() for line in inp]

    print(find_similar_box_ids(box_ids))  # revtaubfniyhsgxdoajwkqilp
