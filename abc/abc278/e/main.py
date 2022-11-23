#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from math import inf


def main():
    H, W, N, h, w = map(int, input().split())
    base_cnt = Counter()
    S = [[[0] * (W + 1) for _ in range(H + 1)] for _ in range(N + 1)]
    for i in range(H):
        a = list(map(int, input().split()))
        for j in range(W):
            S[a[j]][i + 1][j + 1] += 1
        base_cnt += Counter(a)

    for i in range(1, N + 1):
        for j in range(H + 1):
            for k in range(1, W + 1):
                S[i][j][k] += S[i][j][k - 1]
    for i in range(1, N + 1):
        for j in range(1, H + 1):
            for k in range(W + 1):
                S[i][j][k] += S[i][j - 1][k]

    ans = [[0] * (W - w + 1) for _ in range(H - h + 1)]
    for i in range(1, N + 1):
        for j in range(H):
            if j + h > H:
                break
            for k in range(W):
                if k + w > W:
                    break
                val = S[i][j][k] + S[i][j + h][k + w]
                val -= S[i][j][k + w] + S[i][j + h][k]
                if base_cnt[i] - val > 0:
                    ans[j][k] += 1
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
