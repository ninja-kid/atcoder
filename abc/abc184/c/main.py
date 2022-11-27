#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    # 0
    if a == c and b == d:
        print(0)
        return

    # 1
    if a + b == c + d or a - b == c - d:
        print(1)
        return
    if abs(a - c) + abs(b - d) <= 3:
        print(1)
        return

    # 2
    if (a + b) % 2 == (c + d) % 2:
        print(2)
        return
    if abs(a - c) + abs(b - d) <= 6:
        print(2)
        return
    for h in range(-3, 4):
        for w in range(-3, 4):
            if abs(h) + abs(w) > 3:
                continue
            ta = a + h
            tb = b + w
            if ta + tb == c + d or ta - tb == c - d:
                print(2)
                return
    print(3)


if __name__ == "__main__":
    main()
