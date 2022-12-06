#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import gcd, inf


def main():
    A, B, C = map(int, input().split())
    base = gcd(A, gcd(B, C))
    ans = (A + B + C) // base - 3
    print(ans)


if __name__ == "__main__":
    main()
