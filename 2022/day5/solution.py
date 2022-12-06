import re


def move_crates(line, crates):
    line = line.replace("move ", '')
    line = line.replace(" from", '')
    line = line.replace(" to", '')
    amount, from_stack, to_stack = line.split(' ')
    for n in range(int(amount)):
        crates[int(to_stack)-1].insert(0, crates[int(from_stack)-1].pop(0))

    return crates


def move_crates_improved(line, crates):
    line = line.replace("move ", '')
    line = line.replace(" from", '')
    line = line.replace(" to", '')
    amount, from_stack, to_stack = line.split(' ')
    temp_stack = []
    for n in range(int(amount)):
        temp_stack.append(crates[int(from_stack)-1].pop(0))
    crates[int(to_stack)-1][:0] = temp_stack

    return crates


def solution(crates):
    first_boxes = ''
    for stack in crates:
        first_boxes += stack[0]
        first_boxes = first_boxes.replace("[", '')
        first_boxes = first_boxes.replace("]", '')
    return first_boxes


def read_file(file):
    with open(file) as f:
        return map(str.strip, f.readlines())


def crate_lists(crates):
    crate_list = [[], [], [], [], [], [], [], [], []]

    for crate in crates:
        n = 0
        stop = 3
        for start in range(0, 4*9, 4):
            sliced = crate[start:stop]

            if re.search("^\[[A-Z]*\]$", sliced):
                crate_list[n].append(sliced)
            n += 1
            stop += 4

    return crate_list


def get_results(file):
    outputs = [0, 0]

    crates1 = crate_lists(read_file("crate_order.txt"))
    crates2 = crate_lists(read_file("crate_order.txt"))

    lines = read_file(file)
    for line in lines:
        # print(line)
        crates1 = move_crates(line, crates1)
        crates2 = move_crates_improved(line, crates2)
    outputs[0] = solution(crates1)
    outputs[1] = solution(crates2)

    return outputs


def main():

    results = get_results("input.txt")

    print(f"solution 1: {results[0]}")
    print(f"solution 2: {results[1]}")


if __name__ == "__main__":
    main()
