#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from math import inf


def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    S = [[0] * (N + 1) for _ in range(N + 1)]
    for h in range(N):
        for w in range(N):
            S[h + 1][w + 1] += D[h][w]
    for h in range(N + 1):
        for w in range(1, N + 1):
            S[h][w] += S[h][w - 1]
    for h in range(1, N + 1):
        for w in range(N + 1):
            S[h][w] += S[h - 1][w]

    cnt = Counter()
    for h1 in range(N):
        for h2 in range(h1 + 1, N + 1):
            for w1 in range(N):
                for w2 in range(w1 + 1, N + 1):
                    val = S[h1][w1] + S[h2][w2]
                    val -= S[h1][w2] + S[h2][w1]
                    cnt[(h2 - h1) * (w2 - w1)] = max(cnt[(h2 - h1) * (w2 - w1)], val)
    for i in range(1, N * N + 1):
        cnt[i] = max(cnt[i], cnt[i - 1])
    Q = int(input())
    for _ in range(Q):
        p = int(input())
        print(cnt[p])


if __name__ == "__main__":
    main()
