#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    A, B = map(int, input().split())

    def calc(N):
        N = str(N)
        M = len(N)

        dp = [[[0] * 2 for _ in range(2)] for _ in range(M + 1)]
        dp[0][0][0] = 1

        for i in range(M):
            n = int(N[i])
            for j in range(2):
                if j:
                    r = 9
                else:
                    r = n
                for k in range(2):
                    for l in range(r + 1):
                        dp[i + 1][j or l < n][k or l == 4 or l == 9] += dp[i][j][k]
        return dp[-1][0][1] + dp[-1][1][1]

    ans = calc(B) - calc(A - 1)
    print(ans)


if __name__ == "__main__":
    main()
