#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    deg, dis = map(int, input().split())

    W = 0
    dir = ""

    DIR = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]

    if dis < 15:
        W = 0
    elif dis < 93:
        W = 1
    elif dis < 201:
        W = 2
    elif dis < 327:
        W = 3
    elif dis < 477:
        W = 4
    elif dis < 645:
        W = 5
    elif dis < 831:
        W = 6
    elif dis < 1029:
        W = 7
    elif dis < 1245:
        W = 8
    elif dis < 1467:
        W = 9
    elif dis < 1707:
        W = 10
    elif dis < 1959:
        W = 11
    else:
        W = 12

    if W == 0:
        print("C", W)
        return

    deg *= 10
    deg -= 1125
    i = deg // 2250
    dir = DIR[i]
    print(dir, W)

if __name__ == "__main__":
    main()
