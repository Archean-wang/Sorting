def insertion(l):
    length = len(l)
    for i in range(1, length):
        val = l[i]
        j = i - 1
        while l[j] > val:
            l[j + 1] = l[j]
            j -= 1
            if j < 0:
                break
        l[j + 1] = val
    return l


if __name__ == "__main__":
    l = [1, 5, 76, 23, 5, 23, 456, 67, 324, 45, 56, 23]
    print(insertion(l))
