#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    V, T, S, D = map(int, input().split())
    if V * T <= D <= V * S:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
