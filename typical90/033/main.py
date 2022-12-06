#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(H * W)
        return

    ans = ((H + 1) // 2) * ((W + 1) // 2)
    print(ans)


if __name__ == "__main__":
    main()
