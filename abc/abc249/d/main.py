#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = Counter(A)

    def make_divisors(n):
        lower_divisors, upper_divisors = [], []
        i = 1
        while i * i <= n:
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n // i)
            i += 1
        return lower_divisors + upper_divisors[::-1]

    ans = 0
    for a in A:
        yakusus = make_divisors(a)
        for y in yakusus:
            z = a // y
            ans += cnt[y] * cnt[z]
    print(ans)


if __name__ == "__main__":
    main()
