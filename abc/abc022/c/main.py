#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from heapq import heappop, heappush
from math import inf


def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    targets = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        if a == 0:
            targets.append((b, c))
        elif b == 0:
            targets.append((a, c))
        else:
            edges[a].append((b, c))
            edges[b].append((a, c))

    def dijkstra(s):
        que = []
        que.append((0, s))
        dist = [inf] * N
        dist[s] = 0

        while que:
            d, fr = heappop(que)
            if dist[fr] < d:
                continue
            for to, cost in edges[fr]:
                if dist[to] <= dist[fr] + cost:
                    continue
                dist[to] = dist[fr] + cost
                heappush(que, (dist[to], to))
        return dist

    if len(targets) <= 1:
        print(-1)
        return

    dists = []
    for i in range(len(targets)):
        d = dijkstra(targets[i][0])
        dists.append(d)

    ans = inf
    for i in range(len(targets)):
        for j in range(i + 1, len(targets)):
            for k in range(N):
                ans = min(
                    ans, targets[i][1] + targets[j][1] + dists[i][k] + dists[j][k]
                )
    if ans == inf:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()
