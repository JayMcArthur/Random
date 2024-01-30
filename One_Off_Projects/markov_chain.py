from enum import IntEnum


class Items(IntEnum):
    apple = 0
    banana = 1
    carrot = 2
    date = 3
    egg = 4


# Markov Chain
graph = []
# Links
transition_matrix = [
    [Items.apple, Items.banana, 1/2],
    [Items.apple, Items.egg, 1/2],
    [Items.banana, Items.apple, 4/9],
    [Items.banana, Items.carrot, 3/9],
    [Items.banana, Items.date, 2/9],
    [Items.carrot, Items.carrot, 1],
    [Items.date, Items.date, 1],
    [Items.egg, Items.egg, 1]
]
# Start
phi = [0] * len(Items)
phi[Items.apple] = 1


def init_chain(chain_, items_) -> None:
    for i in items_:
        chain_.append([0]*len(items_))


def create_link(chain_, item_a, item_b, probability) -> None:
    chain_[item_a][item_b] = probability


def create_chain(chain_, links_) -> None:
    for link in links_:
        create_link(chain_, *link)


def solve_chain(chain_, start_) -> list:
    step = [*start_]
    start_ = [[0] * len(step)]
    step = [step]
    while sum(abs(a-b) for a,b in zip(*start_, *step)) > 0.000000000000001:
        start_ = [*step]
        step = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*chain_)] for X_row in start_]
    return step


def main() -> None:
    init_chain(graph, Items)
    create_chain(graph, transition_matrix)
    result = solve_chain(graph, phi)
    print(result)
