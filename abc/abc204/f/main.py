#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60

I = []


def malMat(A, B, mod=10**9 + 7):
    ret = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                ret[i][j] += A[i][k] * B[k][j]
                if mod > 0:
                    ret[i][j] %= mod
    return ret


def powMat(A, K, mod=10**9 + 7):
    global I
    if K == 0:
        if not I:
            I = [[0] * len(A[0]) for _ in range(len(A))]
            for i in range(len(A)):
                I[i][i] = 1
        return I
    if K % 2 == 0:
        return powMat(malMat(A, A, mod), K // 2, mod)
    return malMat(A, powMat(A, K - 1, mod), mod)


def main():
    H, W = map(int, input().split())
    N = 1 << H
    A = [[0] * N for _ in range(N)]

    def dfs(S, T, cur):
        if cur == H:
            A[S][T] += 1
            return
        # すでにおいていた場合
        if (S >> cur) & 1:
            dfs(S, T, cur + 1)
            return
        # 大を横に置く
        dfs(S, T + (1 << cur), cur + 1)
        # 小を置く
        dfs(S, T, cur + 1)
        # 大を縦長に置く
        if cur + 1 < H and (S >> (cur + 1)) % 2 == 0:
            dfs(S, T, cur + 2)

    for s in range(1 << H):
        dfs(s, 0, 0)

    result = powMat(A, W, mod2)
    print(result[0][0])


if __name__ == "__main__":
    main()
