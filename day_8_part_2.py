from PIL import Image

from day_8_part_1 import convert_to_layers


def map_layers(layers: dict) -> list:
    image = [0 for x in range(150)]
    for k, v in reversed(layers.items()):
        for i, pixel in enumerate(list(v)):
            if pixel == '2':
                pass
            elif pixel == '0':
                image[i] = 0
            elif pixel == '1':
                image[i] = 256
    return image


def draw(layer_map: list):
    image = Image.new(mode='L', size=(25, 6))
    image.putdata(layer_map)
    image.save('day_8_output.png', 'PNG')


if __name__ == '__main__':
    with open("day_8_input.txt", "r") as f:
        input = f.read().rstrip('\n')
    layers = convert_to_layers(input)
    m = map_layers(layers)
    draw(m)
