#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf
from decimal import Decimal


def main():
    A, B = map(int, input().split())
    def calc(x):
        return B * x + A / (x + 1) ** 0.5

    left = 0
    right = 10**18
    while right - left > 2:
        mid1 = left + (right - left) // 3
        mid2 = left + (right - left) // 3 * 2
        if calc(mid1) <= calc(mid2):
            right = mid2
        else:
            left = mid1
    ans = inf
    for i in range(left, right + 1):
        ans = min(ans, calc(i))
    print(ans)


if __name__ == "__main__":
    main()
