import pathlib

content = pathlib.Path("elf-calories.txt").read_text()
elf_calories = content.split("\n\n")


def _calculate_kcal_per_elf():
    total_kcal_per_elf = {}
    for elf, calorie_line in enumerate(elf_calories, start=1):
        total_kcal_per_elf[elf] = sum(
            int(i) for i in calorie_line.split()
        )
    return total_kcal_per_elf


total_kcal_per_elf = _calculate_kcal_per_elf()


def get_max_kcal_elves():
    return max(
        total_kcal_per_elf.items(), key=lambda x: x[1]
    )[1]


def get_total_kcal_top_elves(n=3):
    top_elves = sorted(
        total_kcal_per_elf.items(), key=lambda x: x[1], reverse=True
    )[:n]
    return sum(x[1] for x in top_elves)
