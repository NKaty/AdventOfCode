import re


def find_sum_values_in_memory(data):
    memory = {}
    new_mask_table = str.maketrans({'X': '1', '1': '0'})
    to_add_table = str.maketrans({'X': '0'})

    for mask, mems in data:
        new_mask = mask.translate(new_mask_table)
        to_add = mask.translate(to_add_table)
        for mem in mems:
            memory[mem[0]] = (mem[1] & int(new_mask, 2)) + int(to_add, 2)

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

    print(find_sum_values_in_memory(docking_data))  # 8332632930672
