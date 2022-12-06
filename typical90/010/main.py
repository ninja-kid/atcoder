#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    stus = [[0] * N for _ in range(2)]
    for i in range(N):
        c, p = map(int, input().split())
        c -= 1
        stus[c][i] = p

    acc = [[0] for _ in range(2)]
    for i in range(N):
        acc[0].append(acc[0][-1] + stus[0][i])
        acc[1].append(acc[1][-1] + stus[1][i])

    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        l -= 1
        a = acc[0][r] - acc[0][l]
        b = acc[1][r] - acc[1][l]
        print(a, b)


if __name__ == "__main__":
    main()
