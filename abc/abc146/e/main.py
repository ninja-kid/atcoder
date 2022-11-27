#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from itertools import accumulate
from math import inf


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    acc = [0]
    for a in A:
        acc.append((acc[-1] + a) % K)

    if K == 1:
        print(A.count(1))
        return

    cnt = Counter()
    ans = 0
    arr = []
    for i in range(N + 1):
        val = (acc[i] - i) % K
        ans += cnt[val]
        cnt[val] += 1
        arr.append(val)
        if i >= K - 1:
            cnt[arr[i - K + 1]] -= 1
    print(ans)


if __name__ == "__main__":
    main()
