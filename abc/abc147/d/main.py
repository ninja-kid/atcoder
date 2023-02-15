py#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))

    one_count = [0] * 60
    for a in A:
        for i in range(60):
            one_count[i] += (a >> i) & 1

    ans = 0
    for i in range(60):
        cnt = one_count[i] * (N - one_count[i]) % mod1
        ans += 2**i * cnt
        ans %= mod1
    print(ans)


if __name__ == "__main__":
    main()
