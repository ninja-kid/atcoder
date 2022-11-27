#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))
    arr = [0]
    for a in A:
        a -= 1
        arr.append(arr[a] + 1)
        arr.append(arr[a] + 1)

    print(*arr, sep="\n")


if __name__ == "__main__":
    main()
