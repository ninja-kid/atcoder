#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dif = 0
    for i in range(N):
        dif += abs(A[i] - B[i])

    if dif <= K and dif % 2 == K % 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
