#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    X = int(input())

    ret = [True] * 10**6
    ret[0] = False
    ret[1] = False
    for i in range(2, 10**6):
        if not ret[i]:
            continue
        for j in range(i + i, 10**6, i):
            ret[j] = False

    for x in range(X, 10**6):
        if ret[x]:
            print(x)
            return


if __name__ == "__main__":
    main()
