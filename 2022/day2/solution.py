def calc_score(cond, shape):
    score = int()
    if shape == 'A':
        score += 1
    elif shape == 'B':
        score += 2
    elif shape == 'C':
        score += 3
    # 0 = loss
    if cond == 0:
        return score
    # 1 = win
    elif cond == 1:
        return score + 6
    elif cond == 2:
        return score + 3


with open('input.txt') as f:
    win = int()
    lines = []
    lines.extend(f.readlines())
    print(lines)
    total_score = int()
    for line in lines:
        y = ''
        o = ''
        line = line.replace('\n', '')
        o, y = line.split(' ')

        #X = lose
        #Y = draw
        #Z = win
        if y == 'X':
            if o == 'A':
                y = 'C'
            elif o == 'B':
                y = 'A'
            elif o == 'C':
                y = 'B'
        elif y == 'Z':
            if o == 'A':
                y = 'B'
            elif o == 'B':
                y = 'C'
            elif o == 'C':
                y = 'A'
        elif y == 'Y':
            y = o
        print(f"{o} {y}")
        # A = rock
        # B = paper
        # C = scissor
        if (o == 'A' and y == 'C') or (o == 'B' and y == 'A') or (o == 'C' and y == 'B'):
            win = 0
        elif y == o:
            win = 2
        elif (o == 'C' and y == 'A') or (o == 'A' and y == 'B') or (o == 'B' and y == 'C'):
            win = 1
        total_score += int(calc_score(win, y))
    print(total_score)
