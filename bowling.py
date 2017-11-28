def score(rolls):
    result = 0
    frame = 1
    in_first_half = True

    for i in range(len(rolls)):
        if rolls[i] == '/':
            result += 10 - last
        else:
            result += grade_roll(rolls[i])
        if frame < 10 and grade_roll(rolls[i]) == 10:
            if rolls[i] == '/':
                result += grade_roll(rolls[i + 1])
            elif rolls[i] == 'X' or rolls[i] == 'x':
                result += grade_roll(rolls[i + 1])
                if rolls[i + 2] == '/':
                    result += 10 - grade_roll(rolls[i + 1])
                else:
                    result += grade_roll(rolls[i + 2])
        last = grade_roll(rolls[i])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if rolls[i] == 'X' or rolls[i] == 'x':
            in_first_half = True
            frame += 1
    return result


def grade_roll(roll):
    if roll in '123456789':
        return int(roll)

    if roll in 'xX/':
        return 10

    if roll == '-':
        return 0

    raise ValueError()
