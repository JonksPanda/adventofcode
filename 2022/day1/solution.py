def solution1(rows):
    calories = []
    temp = []
    for row in rows:
        if row.isnumeric():
            temp.append(int(row))
        else:
            calories.append(sum(temp))
            temp = []

    return max(calories)


def solution2(rows):
    calories = []
    temp = []
    for row in rows:
        if row.isnumeric():
            temp.append(int(row))
        else:
            calories.append(sum(temp))
            temp = []
    calories_sorted = sorted(calories)
    return calories_sorted[-1] + calories_sorted[-2] + calories_sorted[-3]


def read_file(filename):
    with open(filename) as f:
        return list(map(str.strip, f.readlines()))


def main():

    rows = read_file("input.txt")
    print(f"solution 1: {solution1(rows)}")
    print(f"solution 2: {solution2(rows)}")


if __name__ == "__main__":
    main()
