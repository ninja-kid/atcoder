#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import deque
from math import inf


def main():
    H, W = map(int, input().split())
    sy, sx = map(int, input().split())
    sy -= 1
    sx -= 1
    gy, gx = map(int, input().split())
    gy -= 1
    gx -= 1

    C = [input() for _ in range(H)]

    def can_move(h, w):
        return C[h][w] == "."

    def bfs(sh, sw):
        que = deque()
        que.append((sh, sw))
        dist = [[-1] * W for _ in range(H)]
        dist[sh][sw] = 0
        while que:
            fh, fw = que.popleft()
            for i in range(4):
                th = fh + dpos4[i][0]
                tw = fw + dpos4[i][1]
                if dist[th][tw] != -1 or not can_move(th, tw):
                    continue
                dist[th][tw] = dist[fh][fw] + 1
                que.append((th, tw))
        return dist

    dist = bfs(sy, sx)
    ans = dist[gy][gx]
    print(ans)


if __name__ == "__main__":
    main()
