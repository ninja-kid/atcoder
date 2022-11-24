#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    S = input()
    A = int(S[:2])
    B = int(S[2:])
    if 0 < A <= 12 and 0 < B <= 12:
        print("AMBIGUOUS")
    elif 0 < A <= 12:
        print("MMYY")
    elif 0 < B <= 12:
        print("YYMM")
    else:
        print("NA")


if __name__ == "__main__":
    main()
