#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60

I = []


def mulMat(A, B, mod=10**9 + 7):
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
        return powMat(mulMat(A, A, mod), K // 2, mod)
    return mulMat(A, powMat(A, K - 1, mod), mod)


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        edges[x].append(y)
        edges[y].append(x)

    invM = pow(M, mod1 - 2, mod1)
    inv2 = pow(2, mod1 - 2, mod1)
    B = [[0] * N for _ in range(N)]
    for i in range(N):
        L = len(edges[i])
        B[i][i] = (M - L) * invM % mod1 + L * inv2 * invM % mod1
        B[i][i] %= mod1
        for j in edges[i]:
            B[i][j] += inv2 * invM
            B[i][j] %= mod1

    result = powMat(B, K, mod1)
    A = [[a] for a in A]
    ans = mulMat(result, A)
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
