#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    N -= 1

    arr = []
    for i in range(100, 1000):
        for j in range(1000):
            b = i
            a = j
            val = 0
            val += b % 10 + b % 10 * 100
            b //= 10
            val += a % 10 * 10
            a //= 10
            val += b % 10 * (11000)
            b //= 10
            val += a % 10 * 100000
            a //= 10
            val += a % 10 * 1000000
            val += b % 10 * 110000000
            arr.append(val)
    arr.sort()
    print(arr[N])


if __name__ == "__main__":
    main()
