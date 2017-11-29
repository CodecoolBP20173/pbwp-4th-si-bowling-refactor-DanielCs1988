LAST_FRAME = 10


def score(rolls):
    """Takes bowling rolls in a game as a list, calculates and returns the score."""
    result = 0
    # Frame equals round in bowling game. Each round has up to 2 rolls.
    frame = 1
    first_roll_in_frame = True

    for current_roll in range(len(rolls)):

        result += grade_roll(rolls[current_roll])
        if rolls[current_roll] == '/':
            result -= last_try
        last_try = grade_roll(rolls[current_roll])

        if frame < LAST_FRAME and rolls[current_roll] in 'xX/':
            result = calculate_special_rolls(rolls, current_roll, result)

        if not first_roll_in_frame or rolls[current_roll] in 'xX':
            frame += 1
            first_roll_in_frame = True
        else:
            first_roll_in_frame = False

    return result


def calculate_special_rolls(rolls, current_roll, result):
    """Calculates score for special (spare, strike) rolls."""
    result += grade_roll(rolls[current_roll + 1])
    if rolls[current_roll] in 'xX':
        if rolls[current_roll + 2] == '/':
            result += 10 - grade_roll(rolls[current_roll + 1])
        else:
            result += grade_roll(rolls[current_roll + 2])

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
