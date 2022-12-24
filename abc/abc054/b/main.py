#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            ok = True
            for k in range(M):
                for l in range(M):
                    if A[i + k][j + l] != B[k][l]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
