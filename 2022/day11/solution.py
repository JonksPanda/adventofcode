class Monkey:
    def __init__(self, starting_items: list, operation, test, if_true, if_false):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false


def solution1(rows):
    monkeys = []
    starting_items = []
    operation = str()
    test = str()
    if_true = int()
    if_false = int()
    for row in rows:
        if row.split(': ')[0] == "Starting items":
            items = row.split(': ')[1].replace(',', '')
            starting_items.extend(items.split(' '))
        elif row.split(': ')[0] == "Operation":
            operation = row.split(': ')[1].replace("new = ", "")
        elif row.split(': ')[0] == "Test":
            test = int(row.split(': ')[1].replace("divisible by ", ""))
        elif row.split(': ')[0] == "If true":
            if_true = int(row.split(': ')[1].replace("throw to monkey ", ''))
        elif row.split(': ')[0] == "If false":
            if_false = int(row.split(': ')[1].replace("throw to monkey ", ''))
            monkeys.append(
                Monkey(starting_items, operation, test, if_true, if_false))
            # resets variables
            starting_items = []
            operation = str()
            test = str()
            if_true = int()
            if_false = int()
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
