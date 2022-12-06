#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, K, M = map(int, input().split())

    if M % mod2 == 0:
        print(0)
        return

    a = pow(K, N, mod2 - 1)
    ans = pow(M, a, mod2)
    print(ans)


if __name__ == "__main__":
    main()
