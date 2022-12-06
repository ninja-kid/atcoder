#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    C = [1 << 60] + list(map(int, input().split()))

    min_price = min(C)
    min_val = -1
    for i in range(10):
        if C[i] == min_price:
            min_val = i

    keta = N // min_price
    remain = N - keta * min_price
    ans = [min_val] * keta
    for i in range(keta):
        if remain <= 0:
            break
        for j in range(9, min_val, -1):
            if remain + min_price < C[j]:
                continue
            ans[i] = j
            remain += min_price
            remain -= C[j]
            break
    print(*ans, sep="")


if __name__ == "__main__":
    main()
