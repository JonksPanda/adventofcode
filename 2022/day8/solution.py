from threading import Thread


class Tree:
    def __init__(self, size, pos) -> None:
        self.size = size
        self.pos = pos
        self.visible = False

    def compare_size(self, map):
        visible = False
        for i in range(len(map)):
            if map[i][self.pos[0]].size < self.size and i < self.pos[1]:
                visible = True
            elif map[i][self.pos[0]].size >= self.size and i < self.pos[1]:
                visible = False
                break
        if visible is False:
            for i in range(self.pos[1], len(map)):
                if map[i][self.pos[0]].size < self.size and i > self.pos[1]:
                    visible = True
                elif map[i][self.pos[0]].size >= self.size and i > self.pos[1]:
                    visible = False
                    break
        if visible is False:
            for row in map:
                for i in range(len(row)):
                    if map[self.pos[1]][i].size < self.size and i < self.pos[0]:
                        visible = True
                    elif map[self.pos[1]][i].size >= self.size and i < self.pos[0]:
                        visible = False
                        break
                break
        if visible is False:
            for row in map:
                for i in range(len(row)):
                    if map[self.pos[1]][i].size < self.size and i > self.pos[0]:
                        visible = True
                    elif map[self.pos[1]][i].size >= self.size and i > self.pos[0]:
                        visible = False
                        break
                break

        return visible


def solution1(rows):
    map = []
    visible_trees = 0
    y = 0

    for tree_row in rows:
        row = []
        x = 0
        for tree_size in tree_row:
            row.append(Tree(size=int(tree_size), pos=(x, y)))
            x += 1
        y += 1
        map.append(row)

    temp_map = []
    for row in map:
        temp_row = []
        for tree in row:
            if tree.pos[1] == 0 or tree.pos[1] == (len(map) - 1):
                tree.visible = True
            elif tree.pos[0] == 0 or tree.pos[0] == (len(row) - 1):
                tree.visible = True
            elif tree.size > 0:
                tree.visible = tree.compare_size(map)
            if tree.visible == True:
                visible_trees += 1
                temp_row.append("X")
            else:
                temp_row.append(str(tree.size))
        temp_map.append(temp_row)

    print(f"solution 1: {visible_trees}")


def solution2(rows):
    for row in rows:
        pass
    print(f"solution 2: 0")


def read_file(filename):
    with open(filename) as f:
        return list(map(str.strip, f.readlines()))


def main():
    rows = read_file("input.txt")

    t1 = Thread(target=solution1, args=(rows,))
    t2 = Thread(target=solution2, args=(rows,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
