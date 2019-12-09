with open("day_4_input.txt", "r") as f:
    input = f.read().split('-')
    input = [int(i) for i in input]


def check_for_doubles(i):
    s = str(i)
    if (s[0] == s[1] or
            s[1] == s[2] or
            s[2] == s[3] or
            s[3] == s[4] or
            s[4] == s[5]):
        return True
    else:
        return False


def check_increasing(i):
    s = str(i)
    if (int(s[0]) <= int(s[1]) and
            int(s[1]) <= int(s[2]) and
            int(s[2]) <= int(s[3]) and
            int(s[3]) <= int(s[4]) and
            int(s[4]) <= int(s[5])):
        return True
    else:
        return False


if __name__ == '__main__':
    possible_passwords = []

    for i in range(input[0], input[1]):
        if (check_for_doubles(i) and
                check_increasing(i)):
            possible_passwords.append(i)

    print(len(possible_passwords))
