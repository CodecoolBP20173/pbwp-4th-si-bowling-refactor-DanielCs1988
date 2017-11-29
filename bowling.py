LAST_FRAME = 10


def score(rolls):
    result = 0
    # Frame equals round in bowling game. Each round has up to 2 rolls.
    frame = 1
    first_round_in_frame = True

    for current_roll in range(len(rolls)):
        if rolls[current_roll] == '/':
            result += 10 - last
        else:
            result += grade_roll(rolls[current_roll])

        if frame < LAST_FRAME:
            if rolls[current_roll] in 'xX/':
                result += grade_roll(rolls[current_roll + 1])
            if rolls[current_roll] in 'xX':
                if rolls[current_roll + 2] == '/':
                    result += 10 - grade_roll(rolls[current_roll + 1])
                else:
                    result += grade_roll(rolls[current_roll + 2])
        last = grade_roll(rolls[current_roll])

        if not first_round_in_frame:
            frame += 1
        first_round_in_frame = False if first_round_in_frame else True
        if rolls[current_roll] in 'xX':
            first_round_in_frame = True
            frame += 1

    return result


def grade_roll(roll):
    """Returns the value of a given roll."""

    if roll in '123456789':
        return int(roll)
    if roll in 'xX/':
        return 10
    if roll == '-':
        return 0

    raise ValueError("Invalid roll!")
