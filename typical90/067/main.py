#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, K = input().split()
    K = int(K)

    def eightToTen(S):
        ret = 0
        for s in S:
            ret *= 8
            ret += int(s)
        return ret

    def TenToNine(n):
        ret = []
        while n > 0:
            a = n % 9
            if a == 8:
                a = 5
            ret.append(str(a))
            n //= 9
        if not ret:
            ret.append("0")
        return "".join(ret[::-1])

    for _ in range(K):
        ten = eightToTen(N)
        N = TenToNine(ten)
    print(N)


if __name__ == "__main__":
    main()
