#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    K = int(input())
    print(50)
    base = K // 50
    K %= 50
    ans = [49 + base - K] * 50
    for i in range(K):
        ans[i] = base + 50
    print(*ans)


if __name__ == "__main__":
    main()
