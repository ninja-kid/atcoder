#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    S = []
    SS = []
    for _ in range(N):
        s = input()
        S.append(s)
        val = (ord(s[0]) - 97, ord(s[-1]) - 97)
        SS.append(val)

    dp = [[False] * 26 for _ in range(1 << N)]

    for s in range(1 << N):
        for i in range(26):
            ret = True
            for j in range(N):
                if (s >> j) % 2 == 0 or SS[j][0] != i:
                    continue
                ret &= dp[s - (1 << j)][SS[j][1]]
            dp[s][i] = not ret

    if any(dp[-1]):
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
