#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    rows = [0] * H
    cols = [0] * W
    for h in range(H):
        for w in range(W):
            rows[h] += A[h][w]
            cols[w] += A[h][w]

    ans = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            ans[h][w] = rows[h] + cols[w] - A[h][w]
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
