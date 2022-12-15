from collections import Counter


def _parse_numbers(data):
    return [[int(i) for i in r] for r in data.splitlines()]


def solution_part1(data: str) -> int:
    nums = _parse_numbers(data)
    # transpose matrix
    nums = list(zip(*nums))
    gamma, epsilon = "", ""
    for n in nums:
        cnt = Counter(n).most_common()
        gamma += str(cnt[0][0])
        epsilon += str(cnt[-1][0])
    return int(gamma, 2) * int(epsilon, 2)


def calculate_rating(nums, *, target_number=1):
    def _get_most_common(index):
        col = [row[index] for row in nums]
        cnt = Counter(col).most_common()

        # if same most commoncounts take target number
        if all(cnt[0][1] == c[1] for c in cnt):
            lookfor = target_number
        else:
            cindex = 0 if target_number else -1
            lookfor = cnt[cindex][0]

        return [row for row in nums if row[index] == lookfor]

    for i in range(nums[0]):
        nums = _get_most_common(i)
        if len(nums) == 1:
            break

    return "".join(map(str, nums[0]))


def solution_part2(data: str) -> int:
    nums = _parse_numbers(data)
    oxygen = calculate_rating(nums)
    co2 = calculate_rating(nums, target_number=0)
    return int(oxygen, 2) * int(co2, 2)
