def quick(l, left, right):
    if left >= right:
        return
    p = left
    q = right
    val = l[right]
    while p < q:
        while p < q and l[p] <= val:
            p += 1
        l[q] = l[p]
        while p < q and l[q] >= val:
            q -= 1
        l[p] = l[q]
    l[p] = val
    quick(l, left, p - 1)
    quick(l, p + 1, right)
    return l


if __name__ == "__main__":
    l = [1, 5, 76, 23, 5, 23, 456, 67, 324, 45, 56, 23]
    print(quick(l, 0, len(l)-1))