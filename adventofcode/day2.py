def load_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]


(ROCK, PAPER, SCISSOR) = (1, 2, 3)
opponent = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSOR
}
player = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSOR
}


def is_draw(opponent_play: str, player_play: str) -> bool:
    return opponent[opponent_play] == player[player_play]


def is_won(opponent_play: str, player_play: str) -> bool:
    if player[player_play] == ROCK and opponent[opponent_play] == SCISSOR:
        return True
    if player[player_play] == SCISSOR and opponent[opponent_play] == ROCK:
        return False
    return player[player_play] > opponent[opponent_play]


def game_score(opponent_play: str, player_play: str) -> int:
    if is_draw(opponent_play, player_play):
        return 3
    if is_won(opponent_play, player_play):
        return 6
    return 0


def solve_part1(data: list[str]) -> int:
    score: int = 0

    for line in data:
        opponent_play = line.split()[0]
        player_play = line.split()[1]
        score += (player[player_play] + game_score(opponent_play, player_play))

    return score


def game_score_part2(opponent_play: str, player_res: str) -> int:
    score: int = 0
    if player_res == "X":
        # You lose
        score += opponent[opponent_play] - 1 \
            if opponent[opponent_play] > ROCK else SCISSOR
    elif player_res == "Y":
        # You draw
        score += 3
        score += opponent[opponent_play]
    elif player_res == "Z":
        # You win
        score += 6
        score += opponent[opponent_play] + 1 \
            if opponent[opponent_play] < SCISSOR else ROCK

    return score


def solve_part2(data: list[str]) -> int:
    score: int = 0

    for line in data:
        opponent_play = line.split()[0]
        player_res = line.split()[1]
        score += game_score_part2(opponent_play, player_res)

    return score
