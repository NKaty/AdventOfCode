from collections import defaultdict


def count_doors(regex):
    coord = 0, 0
    shifts = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    dist = defaultdict(int)
    intersections = []
    count = 0
    for char in regex:
        if char == '(':
            intersections.append((coord, count))
        elif char == ')':
            coord, count = intersections.pop()
        elif char == '|':
            coord, count = intersections[-1]
        else:
            count += 1
            coord = coord[0] + shifts[char][0], coord[1] + shifts[char][1]
            dist[coord] = count if not dist[coord] else min(dist[coord], count)
    return max(dist.values())


if __name__ == "__main__":
    with open('day20/input.txt') as inp:
        data = inp.read().strip('^$ \n')

    print(count_doors(data))  # 4184

