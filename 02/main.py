from enum import Enum, auto


class Moves(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def beats(self):
        match self:
            case Moves.ROCK:
                return Moves.SCISSORS
            case Moves.PAPER:
                return Moves.ROCK
            case Moves.SCISSORS:
                return Moves.PAPER

    def beats_by(self):
        match self:
            case Moves.ROCK:
                return Moves.PAPER
            case Moves.PAPER:
                return Moves.SCISSORS
            case Moves.SCISSORS:
                return Moves.ROCK

    def move_score(self) -> int:
        match self:
            case Moves.ROCK:
                return 1
            case Moves.PAPER:
                return 2
            case Moves.SCISSORS:
                return 3

    @classmethod
    def to_move(cls, move: str) -> "Moves":
        match move:
            case "A" | "X":
                return Moves.ROCK
            case "B" | "Y":
                return Moves.PAPER
            case "C" | "Z":
                return Moves.SCISSORS
            case _:
                raise ValueError("Invalid move")


def calc_outcome_score(opp_move, my_move: Moves) -> int:
    if opp_move == my_move:  # draw
        return 3
    elif my_move == opp_move.beats_by():  # win
        return 6
    elif my_move == opp_move.beats():  # lose
        return 0
    raise ValueError("Invalid moves")


def preprocess(filename: str) -> list[tuple[str, str]]:
    with open(filename, encoding="utf-8") as f:
        moves = [tuple(line.split()) for line in f.readlines()]
    return moves


def part_one(moves: list[tuple[str, str]]) -> int:
    total = 0
    for elf, me in moves:
        elf_move, my_move = Moves.to_move(elf), Moves.to_move(me)
        total += my_move.move_score()
        total += calc_outcome_score(elf_move, my_move)
    return total


def part_two(moves: list[tuple[str, str]]) -> int:
    total = 0
    for elf, outcome in moves:
        elf_move = Moves.to_move(elf)
        match outcome:
            case "X":  # lose
                my_move = elf_move.beats()
            case "Y":  # draw
                my_move = elf_move
            case "Z":  # win
                my_move = elf_move.beats_by()
            case _:
                raise ValueError("Invalid outcome")
        total += my_move.move_score()
        total += calc_outcome_score(elf_move, my_move)
    return total


def main() -> None:
    moves = preprocess("./input")
    print("---Part One---")
    print(part_one(moves))

    print("---Part One---")
    print(part_two(moves))


if __name__ == "__main__":
    main()
