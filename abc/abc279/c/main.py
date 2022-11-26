#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    H, W = map(int, input().split())
    S = [[] for _ in range(W)]
    for _ in range(H):
        s = input()
        for i in range(W):
            S[i].append(s[i])
    T = [[] for _ in range(W)]
    for _ in range(H):
        t = input()
        for i in range(W):
            T[i].append(t[i])
    SS = ["".join(s) for s in S]
    TT = ["".join(t) for t in T]
    SS.sort()
    TT.sort()
    if SS == TT:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
