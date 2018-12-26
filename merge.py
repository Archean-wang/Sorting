def _merge(l1, l2):
    l = []
    i = j = 0
    len1 = len(l1)
    len2 = len(l2)
    while i < len1 and j < len2:
        if l1[i] <= l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1
    if i == len1:
        l.extend(l2[j:])
    if j == len2:
        l.extend(l1[i:])
    return l


def merge(l):
    length = len(l)
    if length <= 1:
        return l
    mid = length // 2
    return _merge(merge(l[:mid]), merge(l[mid:]))


if __name__ == "__main__":
    l = [1, 5, 76, 23, 5, 23, 456, 67, 324, 45, 56, 23]
    print(merge(l))