#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    S = input()
    target = "atcoder"
    enc = {target[i] : i for i in range(len(target))}
    SS = [enc[s] for s in S]

    ans = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if SS[i] > SS[j]:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
