#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    M, K = map(int, input().split())
    if 2 ** M <= K:
        print(-1)
        return
    if M == 0:
        print(0, 0)
        return
    if M == 1:
        if K == 1:
            print(-1)
        else:
            print(0, 0, 1, 1)
        return
    
    A = []
    for i in range(2**(M)):
        if i == K:
            continue
        A.append(i)
    ans = A + [K] + A[::-1] + [K]
    print(*ans)


if __name__ == "__main__":
    main()
