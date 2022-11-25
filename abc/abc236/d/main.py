#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = [[0] * 2 * N for _ in range(2 * N)]
    for i in range(2 * N - 1):
        a = list(map(int, input().split()))
        for j, aa in enumerate(a):
            A[i][i + j + 1] = aa
            A[i + j + 1][i] = aa

    used = [False] * 2 * N
    vals = []

    def dfs():
        if len(vals) == N:
            ret = 0
            for v in vals:
                ret ^= v
            return ret
        ret = 0
        for i in range(2 * N):
            if used[i]:
                continue
            used[i] = True
            for j in range(i + 1, 2 * N):
                if used[j]:
                    continue
                used[j] = True
                vals.append(A[i][j])
                ret = max(ret, dfs())
                vals.pop()
                used[j] = False
            used[i] = False
            break
        return ret

    ans = dfs()
    print(ans)


if __name__ == "__main__":
    main()
