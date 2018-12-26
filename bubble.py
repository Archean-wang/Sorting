def bubble(l):
    length = len(l)
    for i in range(length - 1):
        j = flag = 0
        while j < length - i - 1:
            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
                flag = True
            if not flag:
                break
            j += 1
    return l


if __name__ == "__main__":
    l = [1, 5, 76, 23, 5, 23, 456, 67, 324, 45, 56, 23]
    print(bubble(l))
