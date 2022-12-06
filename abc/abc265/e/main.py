#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, M = map(int, input().split())
    A, B, C, D, E, F = map(int, input().split())
    shougai = set(tuple(map(int, input().split())) for _ in range(M))

    dp = [[[(0) for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    ans = 0
    for i in range(N + 1):
        for j in range(N + 1):
            if i + j > N:
                break
            for k in range(N + 1):
                if i + j + k > N:
                    break
                x = A * i + C * j + E * k
                y = B * i + D * j + F * k
                if (x, y) in shougai:
                    continue
                if i - 1 >= 0:
                    dp[i][j][k] += dp[i - 1][j][k]
                if j - 1 >= 0:
                    dp[i][j][k] += dp[i][j - 1][k]
                if k - 1 >= 0:
                    dp[i][j][k] += dp[i][j][k - 1]
                dp[i][j][k] %= mod2
                if i + j + k == N:
                    ans += dp[i][j][k]
                    ans %= mod2
    print(ans)


if __name__ == "__main__":
    main()
