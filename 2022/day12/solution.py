def solution1(rows):
    for row in rows:
        pass
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
