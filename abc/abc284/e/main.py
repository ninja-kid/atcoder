#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf

import sys

sys.setrecursionlimit(10**6)


def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    visited = [False] * N

    def dfs(fr, prev=-1):
        ret = 1
        visited[fr] = True
        for to in edges[fr]:
            if to == prev:
                continue
            if visited[to]:
                continue
            ret += dfs(to, fr)
            if ret > 10**6:
                break
        visited[fr] = False
        return min(ret, 10**6)

    ans = dfs(0)
    print(ans)


if __name__ == "__main__":
    main()
