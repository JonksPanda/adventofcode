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


def get_results(filename):
    outputs = [0, 0]

    rows = read_file(filename)

    outputs[0] += solution1(rows)
    outputs[1] += solution2(rows)

    return outputs


def main():

    results = get_results("input.txt")

    print(f"solution 1: {results[0]}")
    print(f"solution 2: {results[1]}")


if __name__ == "__main__":
    main()
