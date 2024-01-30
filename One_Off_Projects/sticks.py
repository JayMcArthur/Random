from copy import deepcopy as dc


def create_states(d) -> None:
    player = []
    for left in range(1, 6):
        for right in range(left, 6):
            player.append(f'{left}{right}')
    for a in player:
        for b in player:
            d[f'{a}{b}'] = {  # Position
                '1': {  # Player
                    'f': [],  # Forward
                    'r': []  # Back
                },
                '2': {
                    'f': [],
                    'r': []
                },
            }


def create_links(d) -> None:
    for key in d.keys():
        p1_m = [int(key[0]), int(key[1])]
        p2_m = [int(key[2]), int(key[3])]

        left = 0
        right = 1

        for i in p1_m:
            if i == 5:
                continue
            if p2_m[left] != 5:
                result = (i + p2_m[left] - 1) % 5 + 1
                if result > p2_m[right]:
                    link = int(f'{p1_m[left]}{p1_m[right]}{p2_m[right]}{result}')
                else:
                    link = int(f'{p1_m[left]}{p1_m[right]}{result}{p2_m[right]}')
                d[key]['1']['f'].append(link)
                d[f'{link}']['2']['r'].append(key)
            if p2_m[right] != 5 and p2_m[left] != p2_m[right]:
                result = (i + p2_m[right] - 1) % 5 + 1
                if result < p2_m[left]:
                    link = int(f'{p1_m[left]}{p1_m[right]}{result}{p2_m[left]}')
                else:
                    link = int(f'{p1_m[left]}{p1_m[right]}{p2_m[left]}{result}')
                d[key]['1']['f'].append(link)
                d[f'{link}']['2']['r'].append(key)
            if p1_m[left] == p1_m[right]:
                break

        for i in p2_m:
            if i == 5:
                continue
            if p1_m[left] != 5:
                result = (i + p1_m[left] - 1) % 5 + 1
                if result > p1_m[right]:
                    link = int(f'{p1_m[right]}{result}{p2_m[left]}{p2_m[right]}')
                else:
                    link = int(f'{result}{p1_m[right]}{p2_m[left]}{p2_m[right]}')
                d[key]['2']['f'].append(link)
                d[f'{link}']['1']['r'].append(key)
            if p1_m[right] != 5 and p1_m[left] != p1_m[right]:
                result = (i + p1_m[right] - 1) % 5 + 1
                if result < p1_m[left]:
                    link = int(f'{(i + p1_m[right] - 1) % 5 + 1}{p1_m[left]}{p2_m[left]}{p2_m[right]}')
                else:
                    link = int(f'{p1_m[left]}{(i + p1_m[right] - 1) % 5 + 1}{p2_m[left]}{p2_m[right]}')
                d[key]['2']['f'].append(link)
                d[f'{link}']['1']['r'].append(key)
            if p2_m[left] == p2_m[right]:
                break


def find_turn(d) -> dict:
    start_pos = 1111
    start_player = '1'
    stack = [{
        'pos': 1111,
        'player': '1',
        'turn': 0}]
    swap = {
        '1': '2',
        '2': '1'
    }
    turns = {f'{start_pos}': {'1': 0, '2': -1}}
    turns[f'{start_pos}'][start_player] = 0
    while len(stack) > 0:
        for move in d[f'{stack[0]["pos"]}'][stack[0]['player']]['f']:
            if f'{move}' not in turns.keys():
                turns[f'{move}'] = {'1': -1, '2': -1}
            if turns[f'{move}'][swap[stack[0]['player']]] == -1:
                stack.append({'pos': move, 'player': swap[stack[0]['player']], 'turn': stack[0]['turn'] + 1})
                turns[f'{move}'][swap[stack[0]['player']]] = stack[0]['turn'] + 1
            elif turns[f'{move}'][swap[stack[0]['player']]] > stack[0]['turn'] + 1:
                turns[f'{move}'][swap[stack[0]['player']]] = stack[0]['turn'] + 1
        stack.pop(0)
    return turns


def find_forced(d) -> str:
    c = dc(d)
    to_check = []
    paths = {}

    for pos in c.keys():
        if pos[-2:] == '55' and pos != '5555':
            to_check.append({'pos': c[pos]['2']['r'], 'player': '1', 'path': [pos]})
            paths[pos] = {}

    while len(to_check) > 0:
        positions, player, path = to_check[-1]['pos'], to_check[-1]['player'], to_check[-1]['path']
        to_check.pop()
        # print(path)
        if player == '1' and '1111' in positions:
            return str(path)

        for pos in positions:
            if player == '1':
                to_check.append({'pos': c[pos]['1']['r'], 'player': '2', 'path': path + [pos]})
            if player == '2':
                if int(path[-1]) in c[pos]['2']['f']:
                    c[pos]['2']['f'].remove(int(path[-1]))
                    if len(c[path[-1]]['2']['f']) == 0:
                        to_check.append({'pos': c[pos]['2']['r'], 'player': '1', 'path': path + [pos]})

    return 'No Forced Found'


def print_sticks(d, t) -> None:
    for key in d.keys():
        if key in t.keys():
            print(f'{key} : {str(d[key]["1"]["f"]):>24} <{t[key]["1"]:02d} ● {t[key]["2"]:02d}> {str(d[key]["2"]["f"]):<24}')
        else:
            print(f'{key} : {str(d[key]["1"]["f"]):>24} <-1 ● -1> {str(d[key]["2"]["f"]):<24}')


def main() -> None:
    sticks = {}
    create_states(sticks)
    create_links(sticks)
    turns = find_turn(sticks)
    print(find_forced(sticks))
    print_sticks(sticks, turns)
