def get_range(start, stop):
    out = []
    for n in range(int(start), int(stop)+1):
        out.append(n)
    return out


def solution1(list1, list2):
    if (list1[0] in list2) and (list1[-1] in list2) or (list2[0] in list1) and (list2[-1] in list1):
        return 1
    else:
        return 0


def solution2(list1, list2):
    for val in list1:
        if val in list2:
            return 1
    return 0


with open("input.txt") as f:
    lines = f.readlines()
    answer1 = 0
    answer2 = 0
    for line in lines:
        line = line.replace('\n', '')
        range1, range2 = line.split(',')
        range1_list = range1.split('-')
        range2_list = range2.split('-')
        answer1 += solution1(get_range(range1_list[0], range1_list[1]), get_range(
            range2_list[0], range2_list[1]))
        answer2 += solution2(get_range(range1_list[0], range1_list[1]), get_range(
            range2_list[0], range2_list[1]))
    print(f"solution 1: {answer1}")
    print(f"solution 2: {answer2}")
