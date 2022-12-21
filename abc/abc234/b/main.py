#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    def calc_dist(a, b):
        return ((P[a][0] - P[b][0]) ** 2 + (P[a][1] - P[b][1]) ** 2) ** 0.5

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans = max(ans, calc_dist(i, j))
    print(ans)


if __name__ == "__main__":
    main()
