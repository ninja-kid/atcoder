#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, A, B = map(int, input().split())
    S = input()

    ans = inf
    for i in range(N):
        val = A * i
        for j in range(N):
            if j >= N - 1 - j:
                break
            l = j + i
            r = N - 1 - j + i
            l %= N
            r %= N
            if S[l] != S[r]:
                val += B
        ans = min(ans, val)
    print(ans)


if __name__ == "__main__":
    main()
