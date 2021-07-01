
def astypes(line, *types):
    return tuple(map(lambda p: p[0](p[1]),
                     zip(types, line.strip().split(" "))))
