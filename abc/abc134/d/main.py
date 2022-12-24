#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (N + 1)
    for i in range(N, 0, -1):
        val = A[i - 1]
        for j in range(i * 2, N + 1, i):
            val += ans[j]
        ans[i] = val % 2
    print(sum(ans))
    print(*[i for i in range(N + 1) if ans[i]])


if __name__ == "__main__":
    main()
