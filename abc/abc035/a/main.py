#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import gcd, inf


def main():
    W, H = map(int, input().split())
    g = gcd(W, H)
    W //= g
    H //= g

    print(f"{W}:{H}")


if __name__ == "__main__":
    main()
