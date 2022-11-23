#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    R, C = map(int, input().split())
    X, Y = map(int, input().split())
    D, L = map(int, input().split())

    A = (R - X + 1) * (C - Y + 1) % mod1

    fact = [1]
    inv = [1]
    for i in range(1, 1000):
        fact.append(fact[-1] * i % mod1)
        inv.append(pow(fact[-1], mod1 - 2, mod1))

    B = fact[X * Y] * inv[D] % mod1 * inv[L] % mod1 * inv[X * Y - (D + L)] % mod1
    ans = A * B % mod1
    print(ans)


if __name__ == "__main__":
    main()
