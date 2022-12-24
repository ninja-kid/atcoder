#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    S = input()
    N = len(S)
    i = N
    A = ["dream", "dreamer", "erase", "eraser"]
    while i > 0:
        ok = False
        for a in A:
            if S[i - len(a) : i] == a:
                ok = True
                i -= len(a)
                break
        if not ok:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()
