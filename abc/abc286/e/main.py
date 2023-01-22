#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = []
    for _ in range(N):
        arr = []
        s = input()
        for i in range(N):
            val = (inf, inf)
            if s[i] == "Y":
                val = (1, -A[i])
            arr.append(val)
        dp.append(arr)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(
                    dp[i][j], (dp[i][k][0] + dp[k][j][0], dp[i][k][1] + dp[k][j][1])
                )
    Q = int(input())
    for _ in range(Q):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if dp[u][v][0] == inf:
            print("Impossible")
        else:
            print(dp[u][v][0], -dp[u][v][1] + A[u])


if __name__ == "__main__":
    main()
