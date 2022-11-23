#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    base = []
    for i in range(N):
        s = input()
        for j in range(N):
            if s[j] == "#":
                base.append((i, j))
    base.sort()

    A = []
    for i in range(N):
        t = input()
        for j in range(N):
            if t[j] == "#":
                A.append((i, j))

    # #の数が違うったらNG
    if len(base) != len(A):
        print("No")
        return

    def rotate(arr):
        ret = []
        for h, w in arr:
            nw = N - 1 - h
            nh = w
            ret.append((nh, nw))
        ret.sort()
        return ret

    def check(arr):
        hdif = base[0][0] - arr[0][0]
        wdif = base[0][1] - arr[0][1]
        for a, b in zip(arr, base):
            if a[0] + hdif != b[0] or a[1] + wdif != b[1]:
                return False
        return True

    for i in range(4):
        if i > 0:
            A = rotate(A)
        if check(A):
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
