#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    ans = []
    users = set()
    for i in range(1, N + 1):
        s = input()
        if s in users:
            continue
        users.add(s)
        ans.append(i)
    print(*ans)


if __name__ == "__main__":
    main()
