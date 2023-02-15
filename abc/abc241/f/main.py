#!/usr/bin/env python3
from bisect import bisect_left
from collections import defaultdict, deque


dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60


def main():
    H, W, N = map(int, input().split())
    sh, sw = map(int, input().split())
    sh -= 1
    sw -= 1
    gh, gw = map(int, input().split())
    gh -= 1
    gw -= 1
    rows = defaultdict(list)
    cols = defaultdict(list)

    for _ in range(N):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        rows[x].append(y)
        cols[y].append(x)
    for h in rows:
        rows[h].sort()
    for w in cols:
        cols[w].sort()

    que = deque()

    que.append((sh, sw))
    dist = {}
    dist[(sh, sw)] = 0
    while que:
        fh, fw = que.popleft()
        hidx = bisect_left(rows[fh], fw)
        if hidx > 0:
            tw = rows[fh][hidx - 1] + 1
            if (fh, tw) not in dist:
                dist[(fh, tw)] = dist[(fh, fw)] + 1
                que.append((fh, tw))
        if hidx < len(rows[fh]):
            tw = rows[fh][hidx] - 1
            if (fh, tw) not in dist:
                dist[(fh, tw)] = dist[(fh, fw)] + 1
                que.append((fh, tw))
        widx = bisect_left(cols[fw], fh)
        if widx > 0:
            th = cols[fw][widx - 1] + 1
            if (th, fw) not in dist:
                dist[(th, fw)] = dist[(fh, fw)] + 1
                que.append((th, fw))
        if widx < len(cols[fw]):
            th = cols[fw][widx] - 1
            if (th, fw) not in dist:
                dist[(th, fw)] = dist[(fh, fw)] + 1
                que.append((th, fw))
    if (gh, gw) in dist:
        print(dist[(gh, gw)])
    else:
        print(-1)


if __name__ == "__main__":
    main()
