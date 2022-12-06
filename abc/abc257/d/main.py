#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import deque
from math import inf


def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    def bfs(s, x):
        que = deque()
        que.append(s)
        visited = [False] * N
        visited[s] = True
        while que:
            fr = que.popleft()
            frx, fry, frp = P[fr]
            for to in range(N):
                if visited[to]:
                    continue
                tox, toy, top = P[to]
                if frp * x < abs(frx - tox) + abs(fry - toy):
                    continue
                visited[to] = True
                que.append(to)
        return all(visited)

    def check(x):
        for i in range(N):
            if bfs(i, x):
                return True
        return False

    ng = 0
    ok = 10**10
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
