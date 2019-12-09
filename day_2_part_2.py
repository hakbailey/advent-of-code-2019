from day_2_part_1 import solve


def find_values():
    for i in range(0, 99):
        noun = i
        for i in range(0, 99):
            verb = i
            if solve(noun, verb) == 19690720:
                return (noun, verb)


if __name__ == '__main__':
    results = find_values()
    print(100 * results[0] + results[1])
