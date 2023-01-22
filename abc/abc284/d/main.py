#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        for i in range(2, N):
            if N % i != 0:
                continue
            if (N // i) % i == 0:
                p = i
                q = N // i**2
            else:
                q = i
                p = round((N // i) ** 0.5)
            print(p, q)
            break


if __name__ == "__main__":
    main()
