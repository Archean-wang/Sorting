def selection(l):
    length = len(l)
    for i in range(length - 1):
        _min = j = i
        while j < length:
            if l[j] < l[_min]:
                _min = j
            j += 1
        l[i], l[_min] = l[_min], l[i]
    return l


if __name__ == "__main__":
    l = [1, 5, 76, 23, 5, 23, 456, 67, 324, 45, 56, 23]
    print(selection(l))
