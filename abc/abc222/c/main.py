#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, M = map(int, input().split())
    enc = {"G": 0, "C": 1, "P": 2}

    A = []
    for _ in range(2 * N):
        a = [enc[a] for a in list(input())]
        A.append(a)
    L = [[0, i] for i in range(2 * N)]
    for i in range(M):
        for j in range(N):
            a = L[2 * j][1]
            b = L[2 * j + 1][1]
            if A[b][i] == (A[a][i] + 1) % 3:
                L[2 * j][0] += 1
            elif A[a][i] == (A[b][i] + 1) % 3:
                L[2 * j + 1][0] += 1
        L.sort(key=lambda a: [-a[0], a[1]])
    for a, b in L:
        print(b + 1)


if __name__ == "__main__":
    main()
