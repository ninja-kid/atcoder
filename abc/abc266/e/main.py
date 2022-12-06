#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())

    ans = 0
    for _ in range(N):
        nxt = 0
        for i in range(1, 7):
            if i < ans:
                nxt += ans * 1 / 6
            else:
                nxt += i * 1 / 6
        ans = nxt
    print(ans)


if __name__ == "__main__":
    main()
