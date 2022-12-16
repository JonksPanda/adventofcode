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
    cycles = []
    monitor = []
    for i in range(5):
        temp = []
        for i in range(39):
            temp.append(".")
        monitor.append(temp)
    for row in rows:
        if row == "noop":
            cycles.append(x)
        else:
            for i in range(2):
                cycles.append(x)
                if i == 1:
                    x += int(row.split(" ")[1])
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
