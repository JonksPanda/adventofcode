#1 get input from file
#2 split strings
#3 compare strings (compartments)
#4 set priority
from string import ascii_lowercase, ascii_uppercase

def find_matching(string1, string2):
    for char in string1:
        if char in string2:
            return char

def find_groups_matching(string1, string2, string3):
    for char in string1:
        if char in string2 and char in string3:
            return char

def get_value(input):
    value = {}
    n = 0
    chars = ascii_lowercase + ascii_uppercase
    for char in chars:
        n+=1
        value.update({char:n})
    return value[input]

def solution1(lines):
    total_score = int()
    for line in lines:
        line = line.replace('\n', '')
        n = int(len(line)/2)
        comp1 = line[:n:]
        comp2 = line[n:]
        matching = find_matching(comp1, comp2)
        score = get_value(matching)
        total_score += score
    return total_score

def solution2(lines):
    total_score = 0
    group = []
    for line in lines:
        line = line.replace('\n', '')
        if len(group) < 2:
            group.append(line)
        else:
            group.append(line)
            matching = find_groups_matching(group[0], group[1], group[2])
            total_score += get_value(matching)
            group = []
    return total_score

with open("input.txt") as f:
    lines = f.readlines()
    print(f"puzzle 1: {solution1(lines)}")
    print(f"puzzle 2: {solution2(lines)}")


        