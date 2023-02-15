#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60


def main():
    N = int(input())
    S = [int(input()) for _ in range(N)]
    M = 10010
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        s = S[i]
        for j in range(M + 1):
            if not dp[i][j]:
                continue
            dp[i + 1][j] = True
            dp[i + 1][j + s] = True
    for j in range(M, -1, -1):
        if dp[-1][j] and j % 10 != 0 or j == 0:
            print(j)
            return


if __name__ == "__main__":
    main()
