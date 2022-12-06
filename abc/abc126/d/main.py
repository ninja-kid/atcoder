#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import deque
from math import inf


def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append((v, w))
        edges[v].append((u, w))

    def bfs(s):
        que = deque()
        que.append(s)
        col = [-1] * N
        col[s] = 0
        while que:
            fr = que.popleft()
            for to, dist in edges[fr]:
                if col[to] != -1:
                    continue
                col[to] = (col[fr] + dist) % 2
                que.append(to)
        return col

    ans = bfs(0)
    print(*ans)


if __name__ == "__main__":
    main()
