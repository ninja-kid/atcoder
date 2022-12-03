#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from heapq import heappop, heappush
from math import inf


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    cost = [0] * N
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
        cost[u] += A[v]
        cost[v] += A[u]

    removed = [False] * N
    que = []
    for i in range(N):
        heappush(que, (cost[i], i))

    remove_count = 0
    ans = 0
    while remove_count < N:
        c, fr = heappop(que)
        if removed[fr]:
            continue
        removed[fr] = True
        remove_count += 1
        ans = max(ans, c)
        for to in edges[fr]:
            cost[to] -= A[fr]
            heappush(que, (cost[to], to))
    print(ans)


if __name__ == "__main__":
    main()
