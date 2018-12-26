def radix(l, maxlen):
    c = 0
    while c < maxlen:
        _l = [[], [], [], [], [], [], [], [], [], []]
        for i in l:
            ge = i // pow(10, c) % 10
            _l[ge].append(i)
        l.clear()
        for j in _l:
            for z in j:
                l.append(z)
        c += 1
    return l


if __name__ == "__main__":
    l = [1, 5, 76, 23, 5, 23, 456, 67, 324, 45, 56, 23]
    print(radix(l, maxlen=3))
