#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from math import inf


def main():
    N = int(input())
    cnt = Counter()
    ans = 0

    def prime_factorize(x):
        ret = []
        while x % 2 == 0:
            ret.append(2)
            x //= 2
        for i in range(3, x + 1, 2):
            if i**2 > x:
                break
            while x % i == 0:
                ret.append(i)
                x //= i
        if x != 1:
            ret.append(x)
        return Counter(ret)

    for i in range(1, N + 1):
        a = prime_factorize(i)
        val = 1
        for k, v in a.items():
            if v % 2 == 0:
                continue
            val *= k
        cnt[val] += 1
    ans = 0
    for v in cnt.values():
        ans += v**2
    print(ans)


if __name__ == "__main__":
    main()
