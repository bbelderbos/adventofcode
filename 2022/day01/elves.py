import pathlib


class ElfCalories:
    def __init__(self, calories_input: pathlib.Path) -> None:
        content = calories_input.read_text()
        self.elf_calories = content.split("\n\n")
        self.total_kcal_per_elf = sorted(self._calculate_kcal_per_elf())

    def _extract_calories(self, line: str) -> int:
        return sum(int(i) for i in line.split())

    def _calculate_kcal_per_elf(self) -> list[int]:
        total_kcal_per_elf = []
        for line in self.elf_calories:
            calories = self._extract_calories(line)
            total_kcal_per_elf.append(calories)
        return total_kcal_per_elf

    def get_max_kcal_elves(self) -> int:
        return self.total_kcal_per_elf[-1]

    def get_total_kcal_top_elves(self, n: int = 3) -> int:
        return sum(self.total_kcal_per_elf[-n:])
