#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, Q = map(int, input().split())
    X = list(range(1, N + 1))
    idxes = [0] + list(range(N))
    for _ in range(Q):
        x = int(input())
        idx = idxes[x]
        if idx == N - 1:
            idxes[X[idx]], idxes[X[idx - 1]] = idxes[X[idx - 1]], idxes[X[idx]]
            X[idx], X[idx - 1] = X[idx - 1], X[idx]
        else:
            idxes[X[idx]], idxes[X[idx + 1]] = idxes[X[idx + 1]], idxes[X[idx]]
            X[idx], X[idx + 1] = X[idx + 1], X[idx]

    print(*X)


if __name__ == "__main__":
    main()
