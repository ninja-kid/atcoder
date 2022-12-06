#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    S = [list(map(int, list(input()))) for _ in range(N)]

    ans = inf
    for i in range(10):
        ss = set()
        for s in S:
            idx = s.index(i)
            while idx in ss:
                idx += 10
            ss.add(idx)
        ans = min(ans, max(ss))
    print(ans)


if __name__ == "__main__":
    main()
