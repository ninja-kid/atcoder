#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf

import sys

sys.setrecursionlimit(10**6)


def main():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))

    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    result = [[] for _ in range(N)]

    def dfs(fr, prev=-1):
        ret = [X[fr]]
        for to in edges[fr]:
            if to == prev:
                continue
            ret += dfs(to, fr)
        ret.sort(reverse=True)
        ret = ret[:20]
        result[fr] = ret
        return ret

    dfs(0)
    for _ in range(Q):
        v, k = map(int, input().split())
        v -= 1
        k -= 1
        print(result[v][k])


if __name__ == "__main__":
    main()
