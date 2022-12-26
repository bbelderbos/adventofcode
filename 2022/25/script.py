def snafu_to_decimal(number: str) -> int:
    symbols = {"=": -2, "-": -1}
    base, total = 5, 0
    for i, n in enumerate(reversed(number)):
        multiplier = int(symbols.get(n, n))
        total += pow(base, i) * multiplier
    return total


def decimal_to_snafu(number: int) -> str:
    base, i = 5, 20  # start somewhere big, might need to increase
    nth = pow(base, i)
    qq = {}
    last = -1
    while i >= 0:
        q, r = divmod(number, nth)
        if last == -1 and q > 0:
            last = i
        qq[nth] = q
        number -= q * nth
        i -= 1
        nth = pow(base, i)

    symbols = {3: "=", 4: "-"}
    carried = 0
    ret = ""
    for i, (nth, amount) in enumerate(sorted(qq.items())):
        amount += carried
        if amount > 4:
            ret = str("0") + ret
            carried = 1
        elif amount < 3:
            ret = str(amount) + ret
            carried = 0
        else:
            symb = symbols[amount]
            ret = symb + ret
            carried = 1
        if i == last:
            break
    return ret


def solution_part1(data: str) -> int:
    snafu_numbers = data.splitlines()
    total = sum(snafu_to_decimal(num) for num in snafu_numbers)
    return decimal_to_snafu(total)


def solution_part2(data: str) -> int:
    pass
