#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    atypes = [0] * N
    btypes = [0] * N
    aset = set()
    bset = set()
    AA = []
    BB = []
    for i in range(N):
        if A[i] not in aset:
            AA.append(A[i])
            aset.add(A[i])
        if B[i] not in bset:
            BB.append(B[i])
            bset.add(B[i])
        atypes[i] = len(aset)
        btypes[i] = len(bset)

    same = [False] * (min(len(aset), len(bset)) + 1)
    xor = set()
    for i in range(min(len(aset), len(bset))):
        if AA[i] in xor:
            xor.remove(AA[i])
        else:
            xor.add(AA[i])
        if BB[i] in xor:
            xor.remove(BB[i])
        else:
            xor.add(BB[i])
        if not xor:
            same[i + 1] = True

    Q = int(input())
    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if atypes[x] != btypes[y]:
            print("No")
            continue
        if same[atypes[x]]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
