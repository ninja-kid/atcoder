#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, M, K, S, T, X = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    S -= 1
    T -= 1
    X -= 1
    dp = [[[0] * 2 for _ in range(N)] for _ in range(K + 1)]
    dp[0][S][0] = 1
    for i in range(K):
        for j in range(N):
            for k in range(2):
                for to in edges[j]:
                    dp[i + 1][to][(k + (to == X)) % 2] += dp[i][j][k]
                    dp[i + 1][to][(k + (to == X)) % 2] %= mod2
    print(dp[-1][T][0])


if __name__ == "__main__":
    main()
