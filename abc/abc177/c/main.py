#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import gcd, inf


def main():
    N = int(input())
    A = list(map(int, input().split()))

    def prime_factorize(x):
        ret = set()
        while x % 2 == 0:
            ret.add(2)
            x //= 2
        for i in range(3, x + 1, 2):
            if i * i > x:
                break
            while x % i == 0:
                ret.add(i)
                x //= i
        if x != 1:
            ret.add(x)
        return ret

    def is_pairwise():
        base = set()
        for a in A:
            s = prime_factorize(a)
            if base & s:
                return False
            base |= s
        return True

    if is_pairwise():
        print("pairwise coprime")
        return

    val = 0
    for a in A:
        val = gcd(val, a)
    if val == 1:
        print("setwise coprime")
        return
    print("not coprime")


if __name__ == "__main__":
    main()
