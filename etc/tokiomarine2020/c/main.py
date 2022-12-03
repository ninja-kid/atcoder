#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split())) + [0]

    for _ in range(K):
        if all([a == N for a in A[:-1]]):
            break
        nxt = [0] * (N + 1)
        for i in range(N):
            a = A[i]
            nxt[max(0, i - a)] += 1
            nxt[min(N, i + a + 1)] -= 1
        for i in range(1, N):
            nxt[i] += nxt[i - 1]
        A = nxt
    print(*A[:-1])


if __name__ == "__main__":
    main()
