#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from math import gcd, inf


def main():
    K = int(input())

    memo = dict()

    def prime_factorize(n):
        if n in memo:
            return memo[n]
        ret = []
        while n % 2 == 0:
            ret.append(2)
            n //= 2
        for i in range(3, n + 1, 2):
            if i * i > n:
                break
            while n % i == 0:
                ret.append(i)
                n //= i
        if n != 1:
            ret.append(n)
        memo[n] = Counter(ret)
        return memo[n]

    cnt = prime_factorize(K)
    ans = 1
    for k, v in cnt.items():
        for i in range(1, v + 1):
            cnt[k] -= 1
            ans = max(ans, k * i)
            aaa = 0
            while i % k == 0:
                aaa += 1
                i //= k
            cnt[k] -= aaa
            if cnt[k] <= 0:
                break
    print(ans)


if __name__ == "__main__":
    main()
