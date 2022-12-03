#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from bisect import bisect_left
from math import inf


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    B.sort(key=lambda a: -a[1])
    fr = 0
    ans = 0
    for b, c in B:
        idx = bisect_left(A, c)
        if idx <= fr:
            break
        if idx - fr <= b:
            ans += (idx - fr) * c
            fr = idx
        else:
            ans += b * c
            fr += b
    for i in range(fr, N):
        ans += A[i]
    print(ans)


if __name__ == "__main__":
    main()
