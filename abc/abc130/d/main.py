#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import deque
from math import inf


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    que = deque()
    ans = (N + 1) * N // 2
    wa = 0
    for a in A:
        que.append(a)
        wa += a
        while que and wa >= K:
            wa -= que.popleft()
        if wa < K:
            ans -= len(que)
    print(ans)


if __name__ == "__main__":
    main()
