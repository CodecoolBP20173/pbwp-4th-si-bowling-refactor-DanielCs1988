LAST_FRAME = 10


def score(rolls):
    result = 0
    frame = 1
    in_first_half = True

    for i in range(len(rolls)):
        if rolls[i] == '/':
            result += 10 - last
        else:
            result += grade_roll(rolls[i])

        if frame < LAST_FRAME:
            if rolls[i] in 'xX/':
                result += grade_roll(rolls[i + 1])
            if rolls[i] in 'xX':
                if rolls[i + 2] == '/':
                    result += 10 - grade_roll(rolls[i + 1])
                else:
                    result += grade_roll(rolls[i + 2])
        last = grade_roll(rolls[i])

        if not in_first_half:
            frame += 1
        in_first_half = False if in_first_half else True
        if rolls[i] in 'xX':
            in_first_half = True
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
