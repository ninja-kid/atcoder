#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import defaultdict
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(1, N + 1):
        dp = [[[0] * i for _ in range(i + 1)] for _ in range(N + 1)]
        dp[0][0][0] = 1
        for j in range(N):
            a = A[j]
            for k in range(i + 1):
                for l in range(i):
                    dp[j + 1][k][l] += dp[j][k][l]
                    dp[j + 1][k][l] %= mod2
                    if k + 1 <= i:
                        dp[j + 1][k + 1][(l + a) % i] += dp[j][k][l]
                        dp[j + 1][k + 1][(l + a) % i] %= mod2
        ans += dp[-1][i][0]
        ans %= mod2
    print(ans)


if __name__ == "__main__":
    main()
