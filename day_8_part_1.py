def convert_to_layers(input: str) -> dict:
    layers = {}
    i = 0
    while i < len(input):
        layer = input[i:i+150]
        layers[int(i/150+1)] = layer
        i += 150
    return layers


def get_min_layer(layers: dict) -> str:
    min = None
    for k, v in layers.items():
        c = v.count('0')
        if not min or c < min[1]:
            min = (k, c)
    return min[0]


if __name__ == '__main__':
    with open("day_8_input.txt", "r") as f:
        input = f.read().rstrip('\n')

    layers = convert_to_layers(input)
    min_key = get_min_layer(layers)
    ones = layers[min_key].count('1')
    twos = layers[min_key].count('2')
    print(ones * twos)
