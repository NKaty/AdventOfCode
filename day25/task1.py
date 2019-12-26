import random
from intcode import process_instructions


def parse_message(message):
    message = message.strip().split('\n')
    count = 0
    place = None
    directions = []
    items = []
    while count < len(message):
        if message[count].startswith('Doors here lead:'):
            count += 1
            while message[count].startswith("-"):
                directions.append(message[count][2:])
                count += 1
        elif message[count].startswith('Items here:'):
            count += 1
            while message[count].startswith("-"):
                items.append(message[count][2:])
                count += 1
        elif message[count].startswith('=='):
            if not place:
                place = message[count]
            count += 1
        else:
            count += 1
    return directions, items, place


def find_password(data):
    # cannot deal with infinite loop at runtime
    dangerous_items = ['infinite loop']
    backs = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}

    def traverse(direction, back):
        message = ''.join(list(map(chr, gen.send(list(map(ord, f'{direction[1]}\n'))))))
        print(message)
        new_directions, new_items, current_place = parse_message(message)

        if current_place is None:
            bad_item = items.pop()
            dangerous_items.append(bad_item)
            raise Exception('Bad item.')

        if current_place not in graph:
            graph[current_place] = direction

        if len(new_items):
            for new_item in new_items:
                if new_item not in dangerous_items:
                    response = gen.send(list(map(ord, f'take {new_item}\n')))
                    if isinstance(response, tuple) and response[1] is None:
                        print(''.join(list(map(chr, response[0]))))
                        dangerous_items.append(new_item)
                        return
                    print(''.join(list(map(chr, response))))
                    items.append(new_item)

        for new_direction in new_directions:
            if new_direction != back and (current_place, new_direction) not in visited:
                visited.add((current_place, new_direction))
                traverse((current_place, new_direction), backs[new_direction])
        print(''.join(list(map(chr, gen.send(list(map(ord, f'{back}\n')))))))

    # go around all the rooms and collect all the items
    # if item is dangerous, put it into dangerous_items for future reference and start again
    while True:
        try:
            items = []
            graph = {}
            visited = set()
            gen = process_instructions(data, [])
            message = ''.join(list(map(chr, next(gen))))
            print(message)
            directions, _, place = parse_message(message)
            if place:
                visited.add(place)

            for direction in directions:
                visited.add((place, direction))
                traverse((place, direction), backs[direction])
        except Exception:
            pass
        else:
            break

    # after collecting the items we're back at the beginning
    # we need to get to Pressure-Sensitive Floor room
    path = []
    place = '== Pressure-Sensitive Floor =='
    while place != '== Hull Breach ==':
        place = graph[place]
        path.append(place[1])
        place = place[0]

    path = path[::-1]
    for direction in path:
        print(''.join(list(map(chr, gen.send(list(map(ord, f'{direction}\n')))))))

    # we're in Pressure-Sensitive Floor room and randomly trying combinations of items
    removed_items = []
    hold_items = items[:]

    while True:
        response = gen.send(list(map(ord, f'{path[-1]}\n')))
        if isinstance(response, tuple) and response[1] is None:
            # the password is in this message
            print(''.join(list(map(chr, response[0]))))
            break
        else:
            message = ''.join(list(map(chr, response)))
            print(message)

        if 'heavier' in message:
            item = random.choice(removed_items)
            removed_items.remove(item)
            hold_items.append(item)
            print(''.join(list(map(chr, gen.send(list(map(ord, f'take {item}\n')))))))
        elif 'lighter' in message:
            item = random.choice(hold_items)
            hold_items.remove(item)
            removed_items.append(item)
            print(''.join(list(map(chr, gen.send(list(map(ord, f'drop {item}\n')))))))


if __name__ == "__main__":
    with open('day25/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    find_password(ns)  # 2214608912
