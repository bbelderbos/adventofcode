import operator as op

ops = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.floordiv,
}


def solution_part1(data: str) -> int:
    monkeys = {}
    for line in data.splitlines():
        m, oper = line.split(": ")
        monkeys[m] = oper

    def _calc(m):
        instr = monkeys[m]
        if instr.isdigit():
            return int(instr)
        else:
            left, o, right = instr.split()
            op = ops[o]
            return op(
                _calc(left),
                _calc(right)
            )

    return _calc("root")


def solution_part2(data: str) -> int:
    pass
