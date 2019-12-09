def opcode(group, full_set):
    new = 0
    if group[0] == 1:
        new = full_set[group[1]] + full_set[group[2]]
    elif group[0] == 2:
        new = full_set[group[1]] * full_set[group[2]]
    full_set[group[3]] = new
    return full_set


def solve(noun, verb):
    with open("day_2_input.txt", "r") as f:
        input = f.read().split(',')

    input = [int(i) for i in input]
    input[1] = noun
    input[2] = verb

    for i in range(0, len(input), 4):
        if input[i] == 99:
            break
        input = opcode(input[i:i+4], input)
    return input[0]


if __name__ == '__main__':
    print(solve(12, 2))
