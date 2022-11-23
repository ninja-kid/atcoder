#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    S = input()

    def check(s):
        if s.lower() == s:
            return False
        if s.upper() == s:
            return False
        if len(s) != len(set(list(s))):
            return False
        return True

    if check(S):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
