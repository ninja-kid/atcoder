#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    m, n, N = map(int, input().split())
    remain = 0
    ans = 0
    while N > 0:
        ans += N
        remain += N
        N = (remain // m) * n
        remain %= m
    print(ans)


if __name__ == "__main__":
    main()
