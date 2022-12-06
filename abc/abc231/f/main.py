#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
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


def shrink(A):
    arr = list(set(A))
    arr.sort()
    enc = {arr[i]: i for i in range(len(arr))}
    return enc


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    encA = shrink(A)
    A = [encA[a] for a in A]
    encB = shrink(B)
    B = [encB[b] for b in B]

    Cs = Counter()
    for i in range(N):
        Cs[(A[i], B[i])] += 1
    C = [[k[0], k[1], v] for k, v in Cs.items()]
    C.sort(key=lambda a: (a[0], -a[1]))

    R = max(B) + 10
    bit = fenwick_tree(R)

    ans = 0
    for a, b, c in C:
        bit.add(b, c)
        ans += c * bit.sum(b, R)

    print(ans)


if __name__ == "__main__":
    main()
