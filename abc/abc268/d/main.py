#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, M = map(int, input().split())
    S = []
    remain = 16 - N + 1
    for _ in range(N):
        s = input()
        remain -= len(s)
        S.append(s)

    T = {input() for _ in range(M)}

    used = [False] * N

    def dfs(ans, remain):
        if all(used):
            if ans not in T and 3 <= len(ans) <= 16:
                print(ans)
                return True
            return False
        if remain > 0:
            if dfs(ans + "_", remain - 1):
                return True
        for i in range(N):
            if used[i]:
                continue
            used[i] = True
            if dfs(ans + "_" + S[i], remain):
                return True
            used[i] = False
        return False

    for i in range(N):
        used[i] = True
        if dfs(S[i], remain):
            return
        used[i] = False
    print(-1)


if __name__ == "__main__":
    main()
