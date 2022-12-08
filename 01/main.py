from heapq import nlargest


def part_one(elf_calories: list[list[int]]) -> int:
    return max(sum(nums) for nums in elf_calories)


def part_two(elf_calories: list[list[int]]) -> int:
    return sum(nlargest(3, (sum(nums) for nums in elf_calories)))


def preprocess(filename: str) -> list[list[int]]:
    with open(filename, encoding="utf-8") as f:
        elves = f.read().split("\n\n")
    return [list(map(int, elf.strip().split("\n"))) for elf in elves]


def main() -> None:
    elf_calories = preprocess("./input")
    print("---Part One---")
    print(part_one(elf_calories))

    print("---Part Two---")
    print(part_two(elf_calories))


if __name__ == "__main__":
    main()
