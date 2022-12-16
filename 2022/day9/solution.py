def adjacent(head, tail):
    # checks if on top
    if (tail[0], tail[1]) == (head[0], head[1]):
        return True
    # checks if adjacent left or right
    elif (tail[0] == (head[0] + 1) or tail[0] == (head[0] - 1)) and tail[1] == head[1]:
        return True
    # checks if adjacent down or up
    elif (tail[1] == (head[1] + 1) or tail[1] == (head[1] - 1)) and tail[0] == head[0]:
        return True
    # checks if upper left/right
    elif (tail[1] == (head[1] + 1) and tail[0] == (head[0] + 1)) or (tail[1] == (head[1] + 1) and tail[0] == (head[0] - 1)):
        return True
    # check if lower left/right
    elif (tail[1] == (head[1] - 1) and tail[0] == (head[0] + 1)) or (tail[1] == (head[1] - 1) and tail[0] == (head[0] - 1)):
        return True
    else:
        return False


def solution1(rows):
    starting_pos = [0, 0]
    head = starting_pos.copy()
    tail = starting_pos.copy()
    unique_positions = []
    for row in rows:
        direction, steps = row.split(" ")
        steps = int(steps)
        for step in range(steps):
            if direction == "D":
                head[1] += 1
            elif direction == "U":
                head[1] -= 1
            elif direction == "R":
                head[0] += 1
            elif direction == "L":
                head[0] -= 1
            if not adjacent(head, tail):
                if tail[1] < head[1]:
                    tail[1] += 1
                if tail[1] > head[1]:
                    tail[1] -= 1
                if tail[0] < head[0]:
                    tail[0] += 1
                if tail[0] > head[0]:
                    tail[0] -= 1
            pos_tail = (tail[0], tail[1])
            if pos_tail not in unique_positions:
                unique_positions.append(pos_tail)
    return len(unique_positions)


def solution2(rows):
    knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
             [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    unique_positions = []
    for row in rows:
        direction, steps = row.split(" ")
        steps = int(steps)
        for step in range(steps):
            if direction == "D":
                knots[0][1] += 1
            elif direction == "U":
                knots[0][1] -= 1
            elif direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1
            for i in range(1, len(knots)):
                if not adjacent(knots[i-1], knots[i]):
                    if knots[i][1] < knots[i-1][1]:
                        knots[i][1] += 1
                    if knots[i][1] > knots[i-1][1]:
                        knots[i][1] -= 1
                    if knots[i][0] < knots[i-1][0]:
                        knots[i][0] += 1
                    if knots[i][0] > knots[i-1][0]:
                        knots[i][0] -= 1
            pos_tail = (knots[9][0], knots[9][1])
            if pos_tail not in unique_positions:
                print(pos_tail)
                unique_positions.append(pos_tail)
    return len(unique_positions)


def read_file(filename):
    with open(filename) as f:
        return list(map(str.strip, f.readlines()))


def main():
    rows = read_file("input.txt")
    print(f"solution 1: {solution1(rows)}")
    print(f"solution 2: {solution2(rows)}")


if __name__ == "__main__":
    main()
