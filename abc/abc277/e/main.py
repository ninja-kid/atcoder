#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import deque
from math import inf


def main():
    N, M, K = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v, a = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append((v, a))
        edges[v].append((u, a))

    S = list(map(int, input().split()))
    switches = [False] * N
    for s in S:
        s -= 1
        switches[s] = True

    def bfs(s, sa):
        que = deque()
        que.append((s, sa, 0))
        dist = [[inf] * 2 for _ in range(N)]
        dist[s][sa] = 0
        while que:
            fr, fa, d = que.popleft()
            if dist[fr][fa] < d:
                continue
            if switches[fr]:
                ta = 1 - fa
                if dist[fr][ta] > d:
                    dist[fr][ta] = d
                    que.appendleft((fr, ta, d))
            for to, ta in edges[fr]:
                if ta != fa:
                    continue
                if dist[to][ta] <= dist[fr][fa] + 1:
                    continue
                dist[to][ta] = d + 1
                que.append((to, ta, d + 1))
        return dist

    dist = bfs(0, 1)
    ans = min(dist[-1])
    if ans == inf:
        ans = -1
    print(ans)

if __name__ == "__main__":
    main()
