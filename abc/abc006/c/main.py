#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, M = map(int, input().split())
    if M < 2 * N or 4 * N < M:
        print(-1, -1, -1)
        return

    tmp = M - 2 * N
    c = tmp // 2
    b = tmp % 2
    a = N - b - c
    print(a, b, c)


if __name__ == "__main__":
    main()
