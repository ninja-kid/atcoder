#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    X = input()

    A = list(X)

    for base in range(int(A[0]), 10):
        for d in range(-9, 10):
            arr = []
            for i in range(len(A)):
                a = base + d * i
                if a < 0 or 10 <= a:
                    break
                arr.append(str(a))
            X = int(''.join(A))
            Y = int(''.join(arr))
            if len(arr) == len(A) and X <= Y:
                print(*arr, sep="")
                return
    print("1" * (len(A) + 1))


if __name__ == "__main__":
    main()
