#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import defaultdict
from math import inf


class fenwick_tree:
    n = 1
    data = [0 for i in range(n)]

    def __init__(self, N):
        self.n = N
        self.data = [0 for i in range(N)]

    def add(self, p, x):
        assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while p <= self.n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l and l <= r and r <= self.n, "0<=l<=r<=n,l={0},r={1},n={2}".format(
            l, r, self.n
        )
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s


def main():
    N = int(input())
    C = list(map(int, input().split()))
    X = list(map(int, input().split()))
    l = sorted(set(X))
    enc = {l[i]: i for i in range(len(l))}
    X = [enc[x] for x in X]
    bit = fenwick_tree(N)

    balls = defaultdict(list)
    for i in range(N):
        balls[C[i]].append(X[i])
    for color in balls:
        l = sorted(set(balls[color]))
        enc = {l[i]: i for i in range(len(l))}
        balls[color] = [enc[a] for a in balls[color]]

    ans = 0
    for x in X[::-1]:
        ans += bit.sum0(x)
        bit.add(x, 1)

    for color in balls:
        bit2 = fenwick_tree(len(balls[color]))
        for x in balls[color][::-1]:
            ans -= bit2.sum0(x)
            bit2.add(x, 1)

    print(ans)


if __name__ == "__main__":
    main()
