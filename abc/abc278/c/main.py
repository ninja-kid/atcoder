#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter, defaultdict
from math import inf


def main():
    N, Q = map(int, input().split())
    rels = defaultdict(Counter)
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            if rels[a][b] == 0:
                rels[a][b] += 1
        elif t == 2:
            if rels[a][b] == 1:
                rels[a][b] -= 1
        else:
            if rels[a][b] == rels[b][a] == 1:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
