def solution1(rows):
    counter = 0
    sequence = []
    for row in rows:
        for char in row:
            counter += 1
            if char in sequence and len(sequence) < 4:
                while char in sequence:
                    sequence.pop(0)
                sequence.append(char)
            else:
                sequence.append(char)
                if len(sequence) == 4:
                    return counter


def solution2(rows):
    counter = 0
    sequence = []
    for row in rows:
        for char in row:
            counter += 1
            #print(char + ': ' + str(counter))
            if char in sequence and len(sequence) < 14:
                while char in sequence:
                    sequence.pop(0)
                sequence.append(char)
            else:
                sequence.append(char)
                if len(sequence) == 14:
                    return counter


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
