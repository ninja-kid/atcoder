#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from math import inf


def main():
    N = int(input())
    cnt = Counter()
    for _ in range(N):
        s = input()
        cnt[s] += 1

    print(cnt.most_common()[0][0])


if __name__ == "__main__":
    main()
