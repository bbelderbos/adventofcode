from collections import Counter
from dataclasses import dataclass, field
from operator import add, mul

OPERATIONS = {"*": mul, "+": add}
BORED_LEVEL = 3
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
        destinations = [int(true[-1]), int(false[-1])]
        m = Monkey(idx, items, op, op_value, test, destinations)
        monkeys.append(m)
    return monkeys


@dataclass
class Monkey:
    idx: int
    items: list[int]
    op: str
    op_value: str
    test: int
    destinations: list[int]
    bored_level: int = BORED_LEVEL

    def __post_init__(self):
        self.op = OPERATIONS[self.op]

    def update_worry_levels(self):
        self.items = [
            self.op(item, item if self.op_value == OLD else int(self.op_value))
            // self.bored_level
            for item in self.items
        ]

    @property
    def to_monkeys(self):
        return [
            self.destinations[0 if item % self.test == 0 else 1] for item in self.items
        ]


@dataclass
class MonkeyManager:
    monkeys: list[Monkey]
    monkey_items: Counter = field(default_factory=Counter)

    def play_round(self):
        for m in self.monkeys:
            m.update_worry_levels()

            for (
                item,
                index,
            ) in zip(m.items, m.to_monkeys):
                self.monkeys[index].items.append(item)

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


def solution_part2(data: str) -> int:
    pass
