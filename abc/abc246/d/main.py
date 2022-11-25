#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())

    def check(x, a):
        return calc(a, x) >= N

    def calc(a, b):
        return a**3 + a**2 * b + a * b**2 + b**3

    ans = inf
    for a in range(10**6 + 1):
        if a**3 > N:
            break
        ok = 10**6 + 1
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if check(mid, a):
                ok = mid
            else:
                ng = mid
        b = ok
        ans = min(ans, calc(a, b))
    print(ans)


if __name__ == "__main__":
    main()
