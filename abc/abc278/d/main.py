#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))
    base = 0
    change = set(range(N))
    Q = int(input())
    for _ in range(Q):
        t, *q = map(int, input().split())
        if t == 1:
            x = q[0]
            base = x
            change = set()
        elif t == 2:
            i, x = q
            i -= 1
            if i in change:
                A[i] += x
            else:
                A[i] = x
                change.add(i)
        else:
            i = q[0]
            i -= 1
            if i in change:
                print(base + A[i])
            else:
                print(base)


if __name__ == "__main__":
    main()
