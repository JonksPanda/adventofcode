class Monkey:
    def __init__(self, items: list, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.times_inspected = 0

    def check_var(self, var, item):
        if var == 'old':
            return int(item)
        else:
            return int(var)

    def test_item(self, item):
        if item % int(self.test) == 0:
            return True
        else:
            return False

    def use_operation(self, item):
        a, operator, b = self.operation.split(" ")
        a = self.check_var(a, item)
        b = self.check_var(b, item)
        if operator == "+":
            return a + b
        elif operator == "*":
            return a * b
        elif operator == "-":
            return a - b
        elif operator == "/":
            return a/b

    def inspect_item(self, item):
        item = self.use_operation(item)
        item = int(item/3)
        if self.test_item(item):
            return item, self.if_true
        else:
            return item, self.if_false


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
    for i in range(20):
        print(i)
        for monkey in monkeys:
            while len(monkey.items) >= 1:
                if monkey.items == 0:
                    break
                new, next = monkey.inspect_item(monkey.items[0])
                monkey.items[0] = new
                monkeys[next].items.append(monkey.items.pop(0))
                monkey.times_inspected += 1
    inspected = []
    for monkey in monkeys:
        inspected.append(monkey.times_inspected)
    inspected.sort()
    print(inspected)
    print(f"{str(inspected[-1])} * {str(inspected[-2])}")
    score = inspected[-1] * inspected[-2]

    return score


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
