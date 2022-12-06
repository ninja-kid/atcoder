#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from bisect import bisect_left
from itertools import accumulate
from math import inf


def main():
    N, Q, X = map(int, input().split())
    W = list(map(int, input().split()))
    total = sum(W)
    W *= 2
    acc = [0] + list(accumulate(W))
    arr = []
    ans = [0] * N
    used = [False] * N
    pos = 0
    Y = X // total
    Z = X % total
    while not used[pos]:
        used[pos] = True
        ans[pos] += Y * N
        arr.append(pos)
        target = acc[pos] + Z
        idx = bisect_left(acc, target)
        ans[pos] += idx - pos
        pos = idx % N

    first = arr.index(pos)
    loop_cnt = len(arr) - first

    for _ in range(Q):
        k = int(input())
        k -= 1
        if k < first:
            print(ans[arr[k]])
            continue
        k -= first
        k %= loop_cnt
        print(ans[arr[first + k]])


if __name__ == "__main__":
    main()
