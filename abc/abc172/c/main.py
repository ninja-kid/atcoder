#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from bisect import bisect_right
from itertools import accumulate
from math import inf


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    accA = [0] + list(accumulate(A))
    accB = [0] + list(accumulate(B))

    ans = 0
    for a in range(N + 1):
        remain = K - accA[a]
        if remain < 0:
            break
        b = bisect_right(accB, remain) - 1
        ans = max(ans, a + b)
    print(ans)


if __name__ == "__main__":
    main()
