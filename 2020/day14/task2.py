import re
from itertools import product


def find_sum_values_in_memory(data):
    memory = {}

    def find_all_addresses(item, m):
        address = list(f'{item[0]:036b}')
        x_ind = []
        for i in range(len(mask)):
            if m[i] == '1':
                address[i] = '1'
            if m[i] == 'X':
                x_ind.append(i)
        combinations = product(range(2), repeat=len(x_ind))
        for combination in combinations:
            current_addr = address[:]
            for i, index in enumerate(x_ind):
                current_addr[index] = str(combination[i])
            memory[''.join(current_addr)] = item[1]

    for mask, mems in data:
        for mem in mems:
            find_all_addresses(mem, mask)

    return sum(memory.values())


if __name__ == "__main__":
    docking_data = []
    mask = None
    mems = []
    reg = r'(\d+)'

    with open('day14/input.txt') as inp:
        for line in inp:
            if line.startswith('mask'):
                if mask is not None:
                    docking_data.append((mask, mems))
                    mems = []
                mask = line.strip()[7:]
            else:
                mems.append(list(map(int, re.findall(reg, line))))
        docking_data.append((mask, mems))

    print(find_sum_values_in_memory(docking_data))  # 4753238784664
