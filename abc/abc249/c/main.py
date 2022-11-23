#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter
from itertools import product
from math import inf


def main():
    N, K = map(int, input().split())

    S = [list(input()) for _ in range(N)]

    ans = 0
    for pro in product([0, 1], repeat=N):
        cnt = Counter()
        for i in range(N):
            if not pro[i]:
                continue
            cnt += Counter(S[i])
        val = 0
        for v in cnt.values():
            val += v == K
        ans = max(ans, val)
    print(ans)


if __name__ == "__main__":
    main()
