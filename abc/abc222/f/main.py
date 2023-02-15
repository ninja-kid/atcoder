#!/usr/bin/env python3
from sys import setrecursionlimit


dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60


def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append((b, c))
        edges[b].append((a, c))
    D = list(map(int, input().split()))

    dp1 = [0] * N
    dp2 = [0] * N

    setrecursionlimit(10**6)

    def dfs1(fr, prev=-1):
        dp1[fr] = 0
        for to, cost in edges[fr]:
            if to == prev:
                continue
            dfs1(to, fr)
            dp1[fr] = max(dp1[fr], max(D[to], dp1[to]) + cost)

    def dfs2(fr, prev=-1):
        dp2[fr] = 0
        n = len(edges[fr])
        lmax = [0] * (n + 1)
        rmax = [0] * (n + 1)
        for i in range(n):
            to, cost = edges[fr][i]
            dp2[fr] = max(dp2[fr], max(D[to], dp1[to]) + cost)
            lmax[i + 1] = max(lmax[i], max(D[to], dp1[to]) + cost)
            j = n - 1 - i
            to, cost = edges[fr][j]
            rmax[j] = max(rmax[j + 1], max(D[to], dp1[to]) + cost)

        for i in range(n):
            to, cost = edges[fr][i]
            if to == prev:
                continue
            dp1[fr] = max(lmax[i], rmax[i + 1])
            dfs2(to, fr)

    dfs1(0)
    dfs2(0)
    print(*dp2)


if __name__ == "__main__":
    main()
