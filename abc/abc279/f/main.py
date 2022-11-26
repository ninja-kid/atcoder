#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


class dsu:
    n = 1
    parent_or_size = [-1 for i in range(n)]

    def __init__(self, N):
        self.n = N
        self.parent_or_size = [-1 for i in range(N)]

    def merge(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        if self.parent_or_size[a] < 0:
            return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [0 for i in range(self.n)]
        group_size = [0 for i in range(self.n)]
        for i in range(self.n):
            leader_buf[i] = self.leader(i)
            group_size[leader_buf[i]] += 1
        result = [[] for i in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        result2 = []
        for i in range(self.n):
            if len(result[i]) > 0:
                result2.append(result[i])
        return result2


def main():
    N, Q = map(int, input().split())
    uf = dsu(N + Q)
    box = list(range(N))
    ball = list(range(N + Q))
    cnt = N
    for _ in range(Q):
        t, *q = map(int, input().split())
        if t == 1:
            x, y = q
            x -= 1
            y -= 1
            if box[y] == -1:
                continue
            if box[x] == -1:
                box[x] = uf.leader(box[y])
                box[y] = -1
                ball[box[x]] = x
            else:
                uf.merge(box[x], box[y])
                box[y] = -1
                ball[uf.leader(box[x])] = x
        elif t == 2:
            x = q[0]
            x -= 1
            if box[x] == -1:
                box[x] = cnt
                ball[cnt] = x
            else:
                uf.merge(box[x], cnt)
                ball[uf.leader(box[x])] = x

            cnt += 1
        else:
            x = q[0]
            x -= 1
            ans = ball[uf.leader(x)] + 1
            print(ans)
        #print([ball[uf.leader(i)] for i in range(cnt)])

if __name__ == "__main__":
    main()
