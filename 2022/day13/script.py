from ast import literal_eval
from itertools import zip_longest


def compare(left, right):
    print("comparing", left, "vs", right)

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("left < right, in order")
            return True
        if left > right:
            print("left > right, not in order")
            return False
        else:
            print("left == right, check next")
            return None

    if isinstance(left, int) and isinstance(right, list):
        print("mixed types, converting left to list")
        return compare([left], right)

    if isinstance(left, list) and isinstance(right, int):
        print("mixed types, converting right to list")
        return compare(left, [right])

    if isinstance(left, list) and isinstance(right, list):
        for i, j in zip_longest(left, right):
            if i is None:
                print("left ran out of items, in order")
                return True
            elif j is None:
                print("right ran out of items, not in order")
                return False
            else:
                ret = compare(i, j)
                if ret is not None:
                    return ret
        return None


def solution_part1(data: str) -> int:
    pairs = data.split("\n\n")
    pair_indices_right_order = []
    for i, pair in enumerate(pairs, start=1):
        print(f"\n---\npair {i}\n---")
        l1, l2 = pair.rstrip().split("\n")
        l1 = literal_eval(l1)
        l2 = literal_eval(l2)
        if compare(l1, l2):
            pair_indices_right_order.append(i)
    print(pair_indices_right_order)
    return sum(pair_indices_right_order)


def solution_part2(data: str) -> int:
    pass
