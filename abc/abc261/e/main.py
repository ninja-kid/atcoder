#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, C = map(int, input().split())
    f = [[0, 1] for _ in range(30)]

    X = C
    for _ in range(N):
        t, A = map(int, input().split())
        nxt = 0
        for i in range(30):
            a = (A >> i) & 1
            if t == 1:
                f[i][0] &= a
                f[i][1] &= a
            elif t == 2:
                f[i][0] |= a
                f[i][1] |= a
            else:
                f[i][0] ^= a
                f[i][1] ^= a
            nxt += f[i][((X >> i) & 1)] << i
        X = nxt
        print(X)


if __name__ == "__main__":
    main()
