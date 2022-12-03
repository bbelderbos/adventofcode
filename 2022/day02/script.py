LOSS, DRAW, WIN = 0, 3, 6
WHO_BEATS_WHO = dict(
    A="C",  # rock beats scissors
    B="A",  # paper beats rock
    C="B",  # scissors beats paper
    X="C",  # rock beats scissors
    Y="A",  # paper beats rock
    Z="B",  # scissors beats paper
)
# a|x = rock, b|y = paper, c|z = scissors
ROLE_POINTS = dict(A=1, B=2, C=3, X=1, Y=2, Z=3)
PLAYER_ALIASES = dict(X="A", Y="B", Z="C")


def get_game_score(opponent, me):
    if me in PLAYER_ALIASES:
        my_rps = PLAYER_ALIASES[me]
    else:
        my_rps = me
    if opponent == my_rps:
        return DRAW
    defeaten = WHO_BEATS_WHO[me]
    if opponent == defeaten:
        return WIN
    return LOSS


def get_score_for_round(line):
    opponent, me = line.split()
    game_score = get_game_score(opponent, me)
    role_score = ROLE_POINTS[me]
    final_score = game_score + role_score
    # print(line, "->", game_score, role_score, final_score)
    return final_score


def _determine_role(opponent, me):
    # x y z = lose draw win
    beaten_by = {v: k for k, v in WHO_BEATS_WHO.items()}
    if me == "Y":
        return opponent
    elif me == "X":
        return WHO_BEATS_WHO[opponent]
    else:
        # win
        return beaten_by[opponent]


def get_score_for_round_part2(line):
    opponent, me = line.split()
    desired_role = _determine_role(opponent, me)
    game_score = get_game_score(opponent, desired_role)
    role_score = ROLE_POINTS[desired_role]
    final_score = game_score + role_score
    # print(line, "->", game_score, role_score, final_score)
    return final_score


def get_total_score_for_all_rounds(lines, *, func=get_score_for_round):
    return sum(func(line) for line in lines)
