#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    A, B, C, D, E, F, X = map(int, input().split())
    taka = X // (A + C) * A * B
    aoki = X // (D + F) * D * E
    xtaka = X % (A + C)
    xaoki = X % (D + F)
    taka += min(xtaka, A) * B
    aoki += min(xaoki, D) * E
    if taka == aoki:
        ans = "Draw"
    elif taka > aoki:
        ans = "Takahashi"
    else:
        ans = "Aoki"
    print(ans)


if __name__ == "__main__":
    main()
