#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    H, W, A, B = map(int, input().split())

    used = [[False] * W for _ in range(H)]
    def dfs(a, hh, ww):
        if a == A:
            return 1
        ret = 0
        for h in range(hh, H):
            for w in range(W):
                if h == hh and w < ww:
                    continue
                if used[h][w]:
                    continue
                used[h][w] = True
                if h + 1 < H and not used[h + 1][w]:
                    used[h + 1][w] = True
                    if w == W - 1:
                        ret += dfs(a + 1, h + 1, 0)
                    else:
                        ret += dfs(a + 1, h, w + 1)
                    used[h + 1][w] = False
                if w + 1 < W and not used[h][w + 1]:
                    used[h][w + 1] = True
                    if w + 2 < W:
                        ret += dfs(a + 1, h, w + 2)
                    else:
                        ret += dfs(a + 1, h + 1, 0)
                    used[h][w + 1] = False
                used[h][w] = False
        return ret
    ans = dfs(0, 0, 0)
    print(ans)

if __name__ == "__main__":
    main()
