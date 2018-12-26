def counting(l, _max):
    length = _max
    _l = [0 for i in range(length + 1)]
    for i in l:
        _l[i] += 1
    l.clear()
    j = 0
    while j <= length:
        for i in range(_l[j]):
            l.append(j)
        j += 1
    return l


if __name__ == "__main__":
    l = [1, 5, 76, 23, 5, 23, 456, 67, 324, 45, 56, 23]
    print(counting(l, 456))