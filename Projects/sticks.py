sticks = {}


def create_states(d) -> None:
    player = []
    for left in range(1, 6):
        for right in range(left, 6):
            player.append(f'{left}{right}')
    for a in player:
        for b in player:
            d[f'{a}{b}'] = [[], []]


def create_links(d) -> None:
    for key in d.keys():
        a = [int(key[0]), int(key[1])]
        b = [int(key[2]), int(key[3])]

        if a == [1, 2] and b == [1, 4]:
            pass

        for i in a:
            if i == 5:
                continue
            if b[0] != 5:
                if (i + b[0] - 1) % 5 + 1 > b[1]:
                    d[key][0].append(int(f'{a[0]}{a[1]}{b[1]}{(i + b[0] - 1) % 5 + 1}'))
                else:
                    d[key][0].append(int(f'{a[0]}{a[1]}{(i + b[0] - 1) % 5 + 1}{b[1]}'))
            if b[1] != 5 and b[0] != b[1]:
                if (i + b[1] - 1) % 5 + 1 < b[0]:
                    d[key][0].append(int(f'{a[0]}{a[1]}{(i + b[1] - 1) % 5 + 1}{b[0]}'))
                else:
                    d[key][0].append(int(f'{a[0]}{a[1]}{b[0]}{(i + b[1] - 1) % 5 + 1}'))
            if a[0] == a[1]:
                break

        for i in b:
            if i == 5:
                continue
            if a[0] != 5:
                if (i + a[0] - 1) % 5 + 1 > a[1]:
                    d[key][1].append(int(f'{a[1]}{(i + a[0] - 1) % 5 + 1}{b[0]}{b[1]}'))
                else:
                    d[key][1].append(int(f'{(i + a[0] - 1) % 5 + 1}{a[1]}{b[0]}{b[1]}'))
            if a[1] != 5 and a[0] != a[1]:
                if (i + a[1] - 1) % 5 + 1 < a[0]:
                    d[key][1].append(int(f'{(i + a[1] - 1) % 5 + 1}{a[0]}{b[0]}{b[1]}'))
                else:
                    d[key][1].append(int(f'{a[0]}{(i + a[1] - 1) % 5 + 1}{b[0]}{b[1]}'))
            if b[0] == b[1]:
                break


def find_turn(d) -> dict:
    start_pos = 1111
    start_player = 0
    stack = [[start_pos, start_player, 1]]
    turns = {f'{start_pos}': [-1, -1]}
    turns[f'{start_pos}'][start_player] = 0
    while len(stack) > 0:
        for move in d[f'{stack[0][0]}'][stack[0][1]]:
            if f'{move}' not in turns.keys():
                turns[f'{move}'] = [-1, -1]
            if turns[f'{move}'][(stack[0][1] + 1) % 2] == -1:
                stack.append([move, (stack[0][1] + 1) % 2, stack[0][2] + 1])
                turns[f'{move}'][(stack[0][1] + 1) % 2] = stack[0][2]
            elif turns[f'{move}'][(stack[0][1] + 1) % 2] > stack[0][2]:
                turns[f'{move}'][(stack[0][1] + 1) % 2] = stack[0][2]
        stack.pop(0)
    return turns


def print_sticks(d, t) -> None:
    for key in d.keys():
        if key in t.keys():
            print(f'{key} : {f"{d[key][0]}":>24} <{t[key][0]:02d} ● {t[key][1]:02d}> {f"{d[key][1]}":<24}')
        else:
            print(f'{key} : {f"{d[key][0]}":>24} <-1 ● -1> {f"{d[key][1]}":<24}')


def main() -> None:
    create_states(sticks)
    create_links(sticks)
    turns = find_turn(sticks)
    print_sticks(sticks, turns)
