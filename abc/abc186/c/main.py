#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if "7" in str(i):
            continue
        ok = True
        while i > 0:
            a = i % 8
            if a == 7:
                ok = False
                break
            i //= 8
        if ok:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
