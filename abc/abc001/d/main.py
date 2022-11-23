#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = []

    def translate(s):
        h = int(s[:2]) * 60
        w = int(s[2:])
        return (h + w)

    for _ in range(N):
        s, e = input().split("-")
        hs = translate(s)
        hs = hs // 5 * 5
        he = translate(e)
        he = (he + 4) // 5 * 5
        A.append((hs, he))
    A.sort()
    ans = []
    for a, b in A:
        if not ans or ans[-1][1] < a:
            ans.append([a, b])
        else:
            ans[-1][1] = max(ans[-1][1], b)
    for a, b in ans:
        ah = a // 60
        aw = a % 60
        bh = b // 60
        bw = b % 60
        aa = str(ah).zfill(2) + str(aw).zfill(2)
        bb = str(bh).zfill(2) + str(bw).zfill(2)
        print(f"{aa}-{bb}")


if __name__ == "__main__":
    main()
