#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from math import inf


def main():
    S = input()
    arr = [Counter()]
    total = Counter()
    for s in S:
        if s == "(":
            arr.append(Counter())
        elif s != ")":
            if total[s] > 0:
                print("No")
                return
            arr[-1][s] += 1
            total[s] += 1
        else:
            total -= arr[-1]
            arr.pop()
    print("Yes")


if __name__ == "__main__":
    main()
