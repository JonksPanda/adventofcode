def solution1(rows):
    x = 1
    cycles = []
    for row in rows:
        if row == "noop":
            cycles.append(x)
        else:
            for i in range(2):
                cycles.append(x)
                if i == 1:
                    x += int(row.split(" ")[1])
    i = 20
    signals = []
    for cycle in cycles[19::40]:
        if i > 220:
            break
        signals.append(cycle * i)
        i += 40
    return sum(signals)


def solution2(rows):
    x = 1
    y = 0
    count = 0
    cycle = 0
    monitor = []
    sprite = []
    for i in range(6):
        temp = []
        for i in range(40):
            temp.append(" ")
        monitor.append(temp)
    for row in rows:
        if count >= 40:
            count = 0
            cycle = 0
            y += 1
        sprite = [x-1, x, x+1]
        if row == "noop":
            if cycle in sprite:
                monitor[y][cycle] = u"\u2588"
            cycle += 1
            count += 1
        else:
            for i in range(2):
                if count >= 40:
                    count = 0
                    cycle = 0
                    y += 1
                if i == 1:
                    x += int(row.split(" ")[1])
                if cycle in sprite:
                    monitor[y][cycle] = u"\u2588"
                cycle += 1
                count += 1

    for y in monitor:
        print(''.join(str(x) for x in y))
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
