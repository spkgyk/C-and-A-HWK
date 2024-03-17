import sys


def possibleNextDigits(d, prev):
    if d == 1:
        r = [2, 4, 5, 6, 8]
        if 2 in prev:
            r += [3]
        if 4 in prev:
            r += [7]
        if 5 in prev:
            r += [9]
        r.sort()
        return r
    elif d == 2:
        r = [1, 3, 4, 5, 6, 7, 9]
        if 5 in prev:
            r += [8]
            r.sort()
        return r
    elif d == 3:
        r = [2, 4, 5, 6, 8]
        if 2 in prev:
            r += [1]
        if 5 in prev:
            r += [7]
        if 6 in prev:
            r += [9]
        r.sort()
        return r
    elif d == 4:
        r = [1, 2, 3, 5, 7, 8, 9]
        if 5 in prev:
            r += [6]
            r.sort()
        return r
    elif d == 5:
        return [1, 2, 3, 4, 6, 7, 8, 9]
    elif d == 6:
        r = [1, 2, 3, 5, 7, 8, 9]
        if 5 in prev:
            r += [4]
            r.sort()
        return r
    elif d == 7:
        r = [2, 4, 5, 6, 8]
        if 4 in prev:
            r += [1]
        if 5 in prev:
            r += [3]
        if 8 in prev:
            r += [9]
        r.sort()
        return r
    elif d == 8:
        r = [1, 3, 4, 5, 6, 7, 9]
        if 5 in prev:
            r += [2]
            r.sort()
        return r
    elif d == 9:
        r = [2, 4, 5, 6, 8]
        if 5 in prev:
            r += [1]
        if 6 in prev:
            r += [3]
        if 8 in prev:
            r += [7]
        r.sort()
        return r


def findPaths(a, b, l, prev):
    l -= 1
    p = prev + [a]
    if a == b:
        if l == 0:
            # print(p)
            return 1
        else:
            return 0
    else:
        nxt = possibleNextDigits(a, p)
        possibleNxt = [x for x in nxt if x not in p]
        k = 0
        for n in possibleNxt:
            k += findPaths(n, b, l, p)
        return k


if __name__ == "__main__":
    a, b, l = sys.stdin.readline().split(" ")

    a = int(a)
    b = int(b)
    l = int(l)

    if a < 1 | b < 1 | a > 9 | b > 9 | l > 9:
        print(0)
    elif a == b:
        print(0)
    else:
        total = findPaths(a, b, l, [])
        print(total)
