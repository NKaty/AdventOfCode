def format_image(image, size):
    if len(image) % (size[0] * size[1]) != 0:
        raise Exception('Broken image.')

    layers = []
    layer = []
    count_row = 0

    for i in range(0, len(image) - size[0] + 1, size[0]):
        layer.append(image[i:i+size[0]])
        count_row += 1
        if count_row == size[1]:
            layers.append(layer)
            layer = []
            count_row = 0

    return layers


def decode_image(image, transparent_pixel):
    visible_pixels = []
    height = len(image[0])
    width = len(image[0][0])
    for row in range(height):
        decoded_row = ''
        for col in range(width):
            for index, layer in enumerate(image):
                if layer[row][col] != transparent_pixel or index == len(image) - 1:
                    decoded_row += layer[row][col]
                    break
        visible_pixels.append(decoded_row)
    return visible_pixels


def print_image(image, color_dict):
    for row in image:
        for pixel in row:
            print(color_dict[pixel], end='')
        print()


if __name__ == "__main__":
    with open('day8/input.txt') as inp:
        img = inp.read().strip()

    formatted_image = format_image(img, (25, 6))
    decoded_image = decode_image(formatted_image, '2')
    print_image(decoded_image, {'0': '\033[30m.\033[0m',  # black
                                '1': '\033[97m.\033[0m',  # white
                                '2': ' '})  # ZFLBY
