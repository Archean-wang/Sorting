def shell(l):
    length = len(l)
    inc = length // 2
    while inc > 0:
        for i in range(inc, length):
            val = l[i]
            j = i - inc
            while l[j] > val:
                l[j + inc] = l[j]
                j -= inc
                if j < 0:
                    break
            l[j + inc] = val
            print(l)
        inc //= 2
    return l


if __name__ == "__main__":
    l = [1, 5, 76, 23, 5, 23, 456, 67, 324, 45, 56, 23]
    print(shell(l))