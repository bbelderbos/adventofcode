from pathlib import Path
from typing import NamedTuple


class File(NamedTuple):
    name: str
    size: int


MAX_DIR_SIZE = 100_000
DISK_SPACE = 70_000_000
FREE_SPACE = 30_000_000

Dirs = dict[Path, list[File]]


def _get_files_per_dir(data: str) -> Dirs:
    root = cwd = Path("/")
    dirs: Dirs = {cwd: []}

    for line in data.strip().splitlines()[1:]:
        if line.startswith("$ cd"):
            dir_name = line.split()[-1]
            if dir_name == "..":
                cwd = cwd.parent
            else:
                cwd /= dir_name
                dirs[cwd] = []

        elif str(line[0]).isdigit():
            size, file_name = line.split()
            file = File(file_name, int(size))

            cwd_copy = cwd
            while True:
                dirs[cwd_copy].append(file)
                cwd_copy = cwd_copy.parent
                if cwd_copy == root:
                    if file not in dirs[root]:
                        dirs[root].append(file)
                    break

    return dirs


def solution_part1(data: str) -> int:
    dir_files = _get_files_per_dir(data)
    total = 0
    for files in dir_files.values():
        dir_size = sum(f.size for f in files)
        if dir_size > MAX_DIR_SIZE:
            continue
        total += dir_size
    return total


def solution_part2(data: str) -> int:
    dir_files = _get_files_per_dir(data)
    dir_sizes = {}

    for d, files in dir_files.items():
        dir_sizes[d] = sum(fi.size for fi in files)
    dir_sizes_sorted = sorted(dir_sizes.values())

    total_root_dir_size = dir_sizes_sorted[-1]
    unused_space = DISK_SPACE - total_root_dir_size
    required_space = FREE_SPACE - unused_space

    for size in dir_sizes_sorted:
        if size > required_space:
            return size
    else:
        raise ValueError(f"No file of at least {required_space=}")
