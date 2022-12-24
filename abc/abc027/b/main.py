#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))

    if sum(A) % N != 0:
        print(-1)
        return

    base = 0
    ans = 0
    target = sum(A) // N
    for i in range(N - 1):
        base += A[i] - target
        if base != 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
