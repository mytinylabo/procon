
def dptable(dim, value):
    return [value] * dim


def dptable2(dims, value):
    return [[value] * dims[1] for _ in range(dims[0])]


def dptable3(dims, value):
    return [[[value] * dims[2] for _ in range[1]] for _ in range(dims[0])]
