#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from heapq import heapify, heappop, heappush
from math import inf


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    que = []
    for a in A:
        heappush(que, -a)

    for _ in range(M):
        val = -heappop(que)
        val //= 2
        heappush(que, -val)
    print(-sum(que))


if __name__ == "__main__":
    main()
