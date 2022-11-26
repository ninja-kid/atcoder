#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    C_base = list(range(N))
    for a in A:
        C_base[a], C_base[a - 1] = C_base[a - 1], C_base[a]
    idx = [-1] * N
    for i in range(N):
        idx[C_base[i]] = i
    C = list(range(N))
    for a in A:
        a -= 1
        target = 0
        if C[a] == target:
            target = C[a + 1]
        elif C[a + 1] == target:
            target = C[a]
        ans = idx[target] + 1
        C[a], C[a + 1] = C[a + 1], C[a]
        print(ans)


if __name__ == "__main__":
    main()
