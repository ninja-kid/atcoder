#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        t, *q = map(int, input().split())
        if t == 1:
            k, x = q
            k -= 1
            A[k] = x
        else:
            k = q[0]
            k -= 1
            print(A[k])


if __name__ == "__main__":
    main()
