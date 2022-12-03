#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, M = map(int, input().split())
    E = [list(map(int, input().split())) for _ in range(M)]
    E.sort(key=lambda a: a[1])
    now = -1
    ans = 0
    for a, b in E:
        if now <= a:
            ans += 1
            now = b
    print(ans)


if __name__ == "__main__":
    main()
