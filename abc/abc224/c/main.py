#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    def gaiseki(a, b, c):
        x1 = P[b][0] - P[a][0]
        y1 = P[b][1] - P[a][1]
        x2 = P[c][0] - P[a][0]
        y2 = P[c][1] - P[a][1]
        return x1 * y2 - x2 * y1

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if gaiseki(i, j, k) != 0:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
