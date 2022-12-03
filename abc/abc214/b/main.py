#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    S, T = map(int, input().split())
    ans = 0
    for a in range(S + 1):
        for b in range(S + 1):
            if a + b > S:
                break
            for c in range(S + 1):
                if a + b + c > S:
                    break
                if a * b * c > T:
                    break
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
