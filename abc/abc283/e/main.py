#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    koritsu = [[] for _ in range(h)]
    for h in range(H):


    def is_inner(h, w):
        return 0 <= h < H and 0 <= w < W

    def dfs(h, push, val, cnt):
        if h == H:
            if len(val):
                return inf
            return min(cnt, H - cnt)

        arr = [set() for _ in range(2)]
        hon = True
        hoff = True
        for w in range(W):
            flg1 = False
            target = A[h - 1][w]
            if push:
                target = 1 - target
            if w in val:
                if target != A[h][w]:
                    hoff = False
                else:
                    hon = False

            if w - 1 >= 0:
                if A[h][w - 1] == A[h][w]:
                    flg1 = True
            if w + 1 < W:
                if A[h][w + 1] == A[h][w]:
                    flg1 = True
            if flg1:
                continue
            if push:
                if 1 - A[h - 1][w] == A[h][w]:
                    arr[1].add(w)
                else:
                    arr[0].add(w)
            else:
                if A[h - 1][w] == A[h][w]:
                    arr[1].add(w)
                else:
                    arr[0].add(w)
        ret = inf
        if hoff:
            ret = min(ret, dfs(h + 1, False, arr[0], cnt))
        if hon:
            ret = min(ret, dfs(h + 1, True, arr[1], cnt + 1))
        return ret

    val = []
    for w in range(W):
        flg = False
        if w - 1 >= 0:
            if A[0][w - 1] == A[0][w]:
                flg = True
        if w + 1 < W:
            if A[0][w + 1] == A[0][w]:
                flg = True
        if not flg:
            val.append(w)
    ans = dfs(1, False, val, 0)
    if ans == inf:
        print(-1)
    else:
        print(min(ans, H - ans))


if __name__ == "__main__":
    main()
