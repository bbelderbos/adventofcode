from collections import Counter
from dataclasses import dataclass, field
from operator import add, mul

OPERATIONS = {"*": mul, "+": add}
OLD = "old"


def _parse_input(data):
    blocks = data.split("\n\n")
    monkeys = []
    for bl in blocks:
        idx, items, op, test, true, false = bl.splitlines()
        idx = int(idx.split()[-1].rstrip(":"))
        items = [int(i) for i in items.split(":")[1].split(",")]
        op, op_value = op.split()[-2:]
        test = int(test.split()[-1])
        dest_true = int(true[-1])
        dest_false = int(false[-1])
        m = Monkey(idx, items, op, op_value, test, dest_true, dest_false)
        monkeys.append(m)
    return monkeys


@dataclass
class Monkey:
    idx: int
    items: list[int]
    op: str
    op_value: str
    test: int
    dest_true: int
    dest_false: int

    def __post_init__(self):
        self.op = OPERATIONS[self.op]

    def update_worry_levels(self, part=1):
        for i, item in enumerate(self.items):
            item2 = item if self.op_value == OLD else int(self.op_value)
            result = self.op(item, item2)
            if part == 1:
                result = result // 3
            self.items[i] = result


@dataclass
class MonkeyManager:
    monkeys: list[Monkey]
    monkey_items: Counter = field(default_factory=Counter)
    part: int = 1

    def play_round(self):
        for m in self.monkeys:
            m.update_worry_levels(part=self.part)

            for item in m.items:
                dest = m.dest_true if item % m.test == 0 else m.dest_false
                self.monkeys[dest].items.append(item)

            self.monkey_items[m.idx] += len(m.items)
            m.items.clear()

    def print_monkeys(self):
        print(*self.monkeys, sep="\n")


def solution_part1(data: str) -> int:
    monkeys = _parse_input(data)
    mm = MonkeyManager(monkeys)
    for _ in range(20):
        mm.play_round()
    top_2 = mm.monkey_items.most_common()[:2]
    return top_2[0][1] * top_2[1][1]


def solution_part2(data: str, rounds=650) -> int:
    monkeys = _parse_input(data)
    mm = MonkeyManager(monkeys, part=2)
    for _ in range(rounds):
        mm.play_round()
    top_2 = mm.monkey_items.most_common()[:2]
    return top_2[0][1] * top_2[1][1]
