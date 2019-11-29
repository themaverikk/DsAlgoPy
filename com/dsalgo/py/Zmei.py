import math


def solve():
    print(n)
    if dbh == -1 or ebh == -1 or x <= 0:
        return 0

    if ebh - ebd >= 0 and dbd < x:
        return -1

    x -= dbd

    if x <= 0:
        return 1

    return math.ceil(1 + x / (ebd - ebh))


t = int(input())

for test in range(t):
    n, x = list(map(int, input().split()))

    dbh = -1
    dbd = -1
    ebh = -1
    ebd = -1

    for i in range(n):
        td, th = list(map(int, input().split()))

        if ebh == -1 or th - td < (ebh - ebd):
            ebh = th
            ebd = td

        if dbh == -1 or td > dbd:
            dbh = th
            dbd = td

    print(solve())
