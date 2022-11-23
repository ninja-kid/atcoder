#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    S = list(input())
    T = list(input())
    at = "atcoder"
    for s, t in zip(S, T):
        if s == t:
            continue
        if s == "@" and t in at:
            continue
        if t == "@" and s in at:
            continue
        print("You will lose")
        return
    print("You can win")


if __name__ == "__main__":
    main()
