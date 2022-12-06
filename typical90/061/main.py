#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import deque
from math import inf


def main():
    Q = int(input())
    que = deque()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            que.appendleft(x)
        elif t == 2:
            que.append(x)
        else:
            x -= 1
            print(que[x])


if __name__ == "__main__":
    main()
