import pathlib

content = pathlib.Path("elf-calories.txt").read_text()
elf_calories = content.split("\n\n")

total_kcal_per_elf = {}
for elf, calorie_line in enumerate(elf_calories, start=1):
    total_kcal_per_elf[elf] = sum(
        int(i) for i in calorie_line.split()
    )


elf_max_kcal = max(
    total_kcal_per_elf.items(), key=lambda x: x[1]
)
print(elf_max_kcal)


top_3 = sorted(total_kcal_per_elf.items(), key=lambda x: x[1], reverse=True)[:3]
total = sum(x[1] for x in top_3)
print(total)
