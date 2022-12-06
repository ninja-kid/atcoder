#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from heapq import heapify, heappop, heappush
from math import inf


def main():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    if sum(A) != L:
        A.append(L - sum(A))

    heapify(A)
    ans = 0
    while len(A) > 1:
        a = heappop(A)
        b = heappop(A)
        ans += a + b
        heappush(A, a + b)
    print(ans)


if __name__ == "__main__":
    main()
