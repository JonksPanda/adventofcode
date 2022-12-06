def solution1(rows):
    calories = []
    temp = []
    for row in rows:
        if row == '':
            n = int()
            for calorie in temp:
                n += calorie
            calories.append(n)
            temp = []
        else:
            temp.append(int(row))
    return max(calories)


def solution2(rows):
    calories = []
    temp = []
    for row in rows:
        if row == '':
            n = int()
            for calorie in temp:
                n += calorie
            calories.append(n)
            temp = []
        else:
            temp.append(int(row))
    calories_sorted = sorted(calories)
    return calories_sorted[-1] + calories_sorted[-2] + calories_sorted[-3]


def read_file(filename):
    with open(filename) as f:
        rows = map(str.strip, f.readlines())
        return rows


def get_results(filename):
    outputs = [0, 0]

    rows = list(read_file(filename))

    outputs[0] += solution1(rows)
    outputs[1] += solution2(rows)

    return outputs


def main():

    results = get_results("input.txt")

    print(f"solution 1: {results[0]}")
    print(f"solution 2: {results[1]}")


if __name__ == "__main__":
    main()
