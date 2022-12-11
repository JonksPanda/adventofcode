class directory:
    def __init__(self, name, parent, layer) -> None:
        self.name = name
        self.subdirs = []
        self.parent_dir = parent
        #self.file_sizes = []
        self.size = 0
        self.layer = layer

    def file_size_sum(self):
        return sum(self.file_sizes)

    def calc_total(self):
        #self.size += sum(self.file_sizes)
        if len(self.subdirs) > 0:
            for sub in self.subdirs:
                self.size += sub.calc_total()
        return self.size


def solution1(rows):
    total = 0
    path = ["/"]
    layer = 1
    max_layer = layer
    dirs = {str(path): directory(name=path, parent=None, layer=1)}
    i = 0
    for row in rows:
        i += 1
        cmd = row.split(" ")
        # check if command

        if cmd[0] == "$":
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    path.pop(-1)
                    layer -= 1
                elif cmd[2] == "/":
                    path = ["/"]
                else:
                    layer += 1
                    new_path = path.copy()
                    new_path.append(cmd[2])
                    if layer > max_layer:
                        max_layer = layer
                    if str(new_path) not in dirs.keys():
                        dirs.update(
                            {str(new_path): directory(name=new_path, parent=dirs[str(path)], layer=layer)})
                        dirs[str(path)].subdirs.append(dirs[str(new_path)])
                    path.append(cmd[2])
                # change and/or create directory
            else:
                continue
        elif cmd[0].isnumeric():
            dirs[str(path)].size += int(cmd[0])
            # input file_size
        # else:
        #     dirs.update(
        #         {cmd[1]: directory(name=cmd[1], parent=pwd, layer=layer+1)})
        #     dirs[pwd].subdirs.append(dirs[cmd[1]])

    dirs[str(["/"])].calc_total()

    for dir in dirs.values():
        if dir.size < 100000:
            total += dir.size
    return total


def solution2(rows):
    path = ["/"]
    layer = 1
    max_layer = layer
    dirs = {str(path): directory(name=path, parent=None, layer=1)}
    i = 0
    for row in rows:
        i += 1
        cmd = row.split(" ")
        # check if command

        if cmd[0] == "$":
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    path.pop(-1)
                    layer -= 1
                elif cmd[2] == "/":
                    path = ["/"]
                else:
                    layer += 1
                    new_path = path.copy()
                    new_path.append(cmd[2])
                    if layer > max_layer:
                        max_layer = layer
                    if str(new_path) not in dirs.keys():
                        dirs.update(
                            {str(new_path): directory(name=new_path, parent=dirs[str(path)], layer=layer)})
                        dirs[str(path)].subdirs.append(dirs[str(new_path)])
                    path.append(cmd[2])
            else:
                continue
        elif cmd[0].isnumeric():
            dirs[str(path)].size += int(cmd[0])
            # input file_size
        # else:
        #     dirs.update(
        #         {cmd[1]: directory(name=cmd[1], parent=pwd, layer=layer+1)})
        #     dirs[pwd].subdirs.append(dirs[cmd[1]])

    dirs[str(["/"])].calc_total()
    space_left = 70000000 - dirs[str(["/"])].size
    diff = 30000000 - space_left
    dir_sizes = []
    for dir in dirs.values():
        if dir.size >= diff:
            dir_sizes.append(dir.size)

    return min(dir_sizes)

    print(rows)
def read_file(filename):
    with open(filename) as f:
        return list(map(str.strip, f.readlines()))


def main():
    rows = read_file("input.txt")
    print(f"solution 1: {solution1(rows)}")
    print(f"solution 2: {solution2(rows)}")


if __name__ == "__main__":
    main()
