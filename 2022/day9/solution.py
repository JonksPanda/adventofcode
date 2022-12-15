def adjacent(head, tail):
    # checks if on top
    if (tail[0], tail[1]) == (head[0], head[1]):
        return True
    # checks if adjacent left or right
    elif tail[0] == (head[0] + 1) or tail[0] == (head[0] - 1):
        return True
    # checks if adjacent down or up
    elif tail[1] == (head[1] + 1) or tail[1] == (head[1] - 1):
        return True
    # checks if upper left/right
    elif (tail[1] == (head[1] + 1) and tail[0] == (head[0] + 1)) or (tail[1] == (head[1] + 1) and tail[0] == (head[0] - 1)):
        return True
    # check if lower left/right
    # elif :
    #     pass
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
        if direction == "D":
            head[1] += steps
        elif direction == "U":
            head[1] -= steps
        elif direction == "R":
            head[0] += steps
        elif direction == "L":
            head[0] -= steps

        print(adjacent(head, tail))

        pos_tail = (tail[0], tail[1])
        if (pos_tail) not in unique_positions:
            print(pos_tail)
            unique_positions.append(pos_tail)
    return 0


def solution2(rows):
    for row in rows:
        pass
    return 0


def read_file(filename):
    with open(filename) as f:
        return list(map(str.strip, f.readlines()))


def main():
    rows = read_file("input.txt")
    print(f"solution 1: {solution1(rows)}")
    print(f"solution 2: {solution2(rows)}")


if __name__ == "__main__":
    main()
