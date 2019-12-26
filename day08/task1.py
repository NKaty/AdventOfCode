import functools
import math


def format_image(image, size):
    layers = []
    num_pixels = size[0] * size[1]

    if len(image) % num_pixels != 0:
        raise Exception('Broken image.')

    for i in range(0, len(image) - num_pixels + 1, num_pixels):
        layers.append(image[i:i+num_pixels])
    return layers


def get_check_value(image, check_digits):
    def find_index_min(acc, item):
        num_of_digit = item[1].count(check_digits[0])
        return (num_of_digit, item[0]) if num_of_digit < acc[0] else acc

    if not len(image):
        raise Exception('Empty image.')

    if len(check_digits) != 3:
        raise Exception('Length of digits for checking must be 3.')

    min_index = functools.reduce(find_index_min, enumerate(image), (math.inf, None))[1]
    return image[min_index].count(check_digits[1]) * image[min_index].count(check_digits[2])


if __name__ == "__main__":
    with open('day08/input.txt') as inp:
        img = inp.read().strip()

    formatted_image = format_image(img, (25, 6))
    print(get_check_value(formatted_image, ('0', '1', '2')))  # 2562
