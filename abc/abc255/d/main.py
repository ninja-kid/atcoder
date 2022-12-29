#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from bisect import bisect_left
from math import inf


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    acc = [0]
    for a in A:
        acc.append(acc[-1] + a)

    for _ in range(Q):
        x = int(input())
        idx = bisect_left(A, x)
        ans = 0
        ans += x * idx - acc[idx]
        ans += acc[-1] - acc[idx] - x * (N - idx)
        print(ans)


if __name__ == "__main__":
    main()
