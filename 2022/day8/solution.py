from threading import Thread
from math import prod


class Tree:
    def __init__(self, size, pos) -> None:
        self.size = size
        self.pos = pos
        self.visible = False
        self.view_score = 0

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

    def get_view_score(self, map):
        score = []

        x = self.pos[0]
        y = self.pos[1]

        # check upper first:
        temp_score = 0
        highest = 0
        for i in range(y-1, -1, -1):
            # if map[i][x].size > highest:
            #     highest = map[y][i].size
            # elif map[i][x].size < highest:
            #     break
            if map[i][x].size < self.size:
                temp_score += 1
            elif map[i][x].size >= self.size:
                temp_score += 1
                break
        if temp_score > 0:
            score.append(temp_score)
        # check down
        temp_score = 0
        highest = 0
        for i in range(y+1, len(map)):
            # if map[i][x].size > highest:
            #     highest = map[y][i].size
            # elif map[i][x].size < highest:
            #     break
            if map[i][x].size < self.size:
                temp_score += 1
            elif map[i][x].size >= self.size:
                temp_score += 1
                break
        if temp_score > 0:
            score.append(temp_score)
        # check left
        temp_score = 0
        highest = 0
        for row in map:
            for i in range(x-1, -1, -1):
                # if map[y][i].size > highest:
                #     highest = map[y][i].size
                # elif map[y][i].size < highest:
                #     break
                if map[y][i].size < self.size:
                    temp_score += 1
                elif map[y][i].size >= self.size:
                    temp_score += 1
                    break
            if temp_score > 0:
                score.append(temp_score)
            break
        # check right
        temp_score = 0
        highest = 0
        for row in map:
            for i in range(x+1, len(row)):
                # if map[y][i].size > highest:
                #     highest = map[y][i].size
                # elif map[y][i].size < highest:
                #     break
                if map[y][i].size < self.size:
                    temp_score += 1
                elif map[y][i].size >= self.size:
                    temp_score += 1
                    break
            if temp_score > 0:
                score.append(temp_score)
            break
        return prod(score)


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
    map = []
    y = 0

    for tree_row in rows:
        row = []
        x = 0
        for tree_size in tree_row:
            row.append(Tree(size=int(tree_size), pos=(x, y)))
            x += 1
        y += 1
        map.append(row)

    scores = []
    for row in map:
        for tree in row:
            if tree.pos[1] == 0 or tree.pos[1] == (len(map) - 1):
                tree.visible = True
            elif tree.pos[0] == 0 or tree.pos[0] == (len(row) - 1):
                tree.visible = True
            elif tree.size > 0:
                tree.visible = tree.compare_size(map)
            if tree.pos[0] > 0 and tree.pos[0] < (len(row) - 1) and tree.pos[1] > 0 and tree.pos[1] < (len(map) - 1):
                tree.view_score = tree.get_view_score(map)
                scores.append(tree.view_score)

    print(f"solution 2: {max(scores)}")


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
