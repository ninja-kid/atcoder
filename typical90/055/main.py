#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        p = A[i] % P
        for j in range(i + 1, N):
            pp = p * A[j] % P
            for k in range(j + 1, N):
                ppp = pp * A[k] % P
                for l in range(k + 1, N):
                    pppp = ppp * A[l] % P
                    for m in range(l + 1, N):
                        if pppp * A[m] % P == Q:
                            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
