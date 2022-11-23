#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf
from timeit import repeat

from itertools import product


def main():
    N, M = map(int, input().split())
    rels = [[False] * N for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        rels[x][y] = True
        rels[y][x] = True

    ans = 0
    for pro in product([0, 1], repeat=N):
        arr = [i for i in range(N) if pro[i]]
        X = len(arr)
        ok = True
        for i in range(X):
            for j in range(i + 1, X):
                if not rels[arr[i]][arr[j]]:
                    ok = False
                    break
        if ok:
            ans = max(ans, X)
    print(ans)


if __name__ == "__main__":
    main()
