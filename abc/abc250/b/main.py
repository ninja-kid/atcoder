#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, A, B = map(int, input().split())
    ans = [["."] * N * B for _ in range(N * A)]
    for i in range(N * A):
        for j in range(N * B):
            h = i // A
            w = j // B
            if (h + w) % 2 == 1:
                ans[i][j] = "#"
    for a in ans:
        print(''.join(a))


if __name__ == "__main__":
    main()
