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
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    dist1 = [0] * N
    cnt1 = [0] * N
    cnt2 = [0] * N
    dist2 = [0] * N

    setrecursionlimit(10**6)

    def dfs1(fr, prev=-1):
        cnt1[fr] = 1
        dist1[fr] = 0
        for to in edges[fr]:
            if to == prev:
                continue
            dfs1(to, fr)
            cnt1[fr] += cnt1[to]
            dist1[fr] += dist1[to] + cnt1[to]

    def dfs2(fr, prev=-1):
        cnt2[fr] = 1
        dist2[fr] = 0
        for to in edges[fr]:
            cnt2[fr] += cnt1[to]
            dist2[fr] += dist1[to] + cnt1[to]

        for to in edges[fr]:
            if to == prev:
                continue
            cnt1[fr] = cnt2[fr] - cnt1[to]
            dist1[fr] = dist2[fr] - (dist1[to] + cnt1[to])
            dfs2(to, fr)

    dfs1(0)
    dfs2(0)
    print(*dist2)


if __name__ == "__main__":
    main()
