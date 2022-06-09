

def main() -> None:
    # item A, Item B, Item C, Item D
    items = [305 + 266, 48 + 4, 279 + 191, 1044 + 1654]
    # 3 Rank G, 5 Rank F, 4 Rank E, 2 Rank D, 1 Rank C, 4 Rank B, 1 Rank A
    people = [3, 5, 4, 2, 1, 4, 1]
    solves = []

    for i in range(len(items)):
        solves.append(solve_claim(people, items[i]))
        print("Item ", i, ": ", solves[i])
        print("Items used: ", sum([a * b for a, b in zip(solves[i], people)]), "/", items[i])


def solve_claim(ppl: list[int], item: int) -> list[int]:
    ranks = [1]
    total = 0

    # Auto generate ranks value
    for i in range(len(ppl) - 1):
        ranks.append(ranks[i] * 1.05)

    # Figure out total we need to divide by to get items worth
    for i in range(len(ranks)):
        total += ranks[i] * ppl[i]
    item_value = item / total

    # reapply items worth to ranks
    for i in range(len(ranks)):
        ranks[i] = round(ranks[i] * item_value)  # Rounding Fix, could just floor

    return ranks
