import pathlib


class ElfCalories:
    def __init__(self, calories_input: pathlib.Path):
        content = calories_input.read_text()
        self.elf_calories = content.split("\n\n")
        self.total_kcal_per_elf = sorted(self._calculate_kcal_per_elf())

    def _calculate_kcal_per_elf(self):
        total_kcal_per_elf = []
        for calorie_line in self.elf_calories:
            total_kcal_per_elf.append(sum(int(i) for i in calorie_line.split()))
        return total_kcal_per_elf

    def get_max_kcal_elves(self):
        return self.total_kcal_per_elf[-1]

    def get_total_kcal_top_elves(self, n=3):
        return sum(self.total_kcal_per_elf[-n:])
