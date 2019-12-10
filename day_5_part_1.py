def opcode(inst, params, output):
    c = get_command(inst)
    n = 0
    i = None

    if c == 1:
        x = get_value(inst, -3, params[0], output)
        y = get_value(inst, -4, params[1], output)
        n = x + y
        output[params[2]] = n
        i = 4
    elif c == 2:
        x = get_value(inst, -3, params[0], output)
        y = get_value(inst, -4, params[1], output)
        n = x * y
        output[params[2]] = n
        i = 4
    if c == 3:
        n = input('Input something: ')
        output[params[0]] = int(n)
        i = 2
    elif c == 4:
        print(output[params[0]])
        i = 2

    return [output, i]


def get_command(inst):
    try:
        return int(inst[-2:])
    except IndexError:
        return int(inst)


def get_value(inst, pos, param, output):
    if is_immediate(inst, pos):
        return param
    else:
        return output[param]


def is_immediate(inst, position):
    try:
        if inst[position] == '1':
            return True
        else:
            return False
    except IndexError:
        return False


def solve():
    with open("day_5_input.txt", "r") as f:
        input = f.read().split(',')
    input = [int(i) for i in input]
    running = True
    i = 0

    while running:
        inst = str(input[i])
        if inst == '99':
            running = False
            break
        params = input[i+1:i+4]
        results = opcode(inst, params, input)
        input = results[0]
        i += results[1]


if __name__ == '__main__':
    solve()

# 13547311
