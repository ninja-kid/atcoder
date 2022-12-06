#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = []
    wa = 0
    for i in range(N):
        ans.append(S[i] - wa)
        wa += ans[-1]
    print(*ans)


if __name__ == "__main__":
    main()
