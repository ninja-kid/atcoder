#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [[False] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        a, b = AB[i]
        for j in range(X + 1):
            if not dp[i][j]:
                continue
            for k in range(b + 1):
                to = j + a * k
                if to <= X:
                    dp[i + 1][to] = True
    if dp[-1][-1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
