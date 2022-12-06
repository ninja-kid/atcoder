#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf

import sys

sys.setrecursionlimit(10**6)


class dsu:
    n = 1
    parent_or_size = [-1 for i in range(n)]

    def __init__(self, N):
        self.n = N
        self.parent_or_size = [-1 for i in range(N)]

    def merge(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        if self.parent_or_size[a] < 0:
            return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [0 for i in range(self.n)]
        group_size = [0 for i in range(self.n)]
        for i in range(self.n):
            leader_buf[i] = self.leader(i)
            group_size[leader_buf[i]] += 1
        result = [[] for i in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        result2 = []
        for i in range(self.n):
            if len(result[i]) > 0:
                result2.append(result[i])
        return result2


def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    E = []
    for _ in range(N):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
        E.append((u, v))

    # ループに含まれる頂点を検出
    used = [False] * N
    path = [-1] * N
    loop = set()

    def dfs(fr, prev=-1):
        used[fr] = True
        for to in edges[fr]:
            if to == prev:
                continue
            path[to] = fr
            if used[to]:
                pos = fr
                while fr != to:
                    loop.add(fr)
                    fr = path[fr]
                loop.add(to)
                return True
            if dfs(to, fr):
                return True
        used[fr] = False
        return False

    dfs(0)
    uf = dsu(N)
    for u, v in E:
        if u in loop and v in loop:
            continue
        uf.merge(u, v)

    Q = int(input())
    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if uf.same(x, y):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
