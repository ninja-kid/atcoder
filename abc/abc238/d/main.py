#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        p = s - 2 * a
        if p < 0:
            print("No")
            continue
        q = a
        ok = True
        for i in range(60):
            if (p >> i) % 2 == (q >> i) % 2 == 1:
                ok = False
                break
        if ok:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
