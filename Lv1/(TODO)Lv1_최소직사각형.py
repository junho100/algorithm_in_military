def solution(sizes):
    sizes = [sorted(i, reverse=True) for i in sizes]

    hor = [i[0] for i in sizes]
    ver = [i[1] for i in sizes]

    return max(hor)*max(ver)