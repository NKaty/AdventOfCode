def find_count_sum(answers):
    return sum(len(set.intersection(*answer)) for answer in answers)


if __name__ == "__main__":
    with open('day06/input.txt') as inp:
        data = ((set(ans) for ans in item.strip().split()) for item in inp.read().split('\n\n'))

    print(find_count_sum(data))  # 3354
