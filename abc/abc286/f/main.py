#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def inv_gcd(a, b):
    a = a % b
    if a == 0:
        return (b, 0)
    s = b
    t = a
    m0 = 0
    m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0:
        m0 += b // s
    return (s, m0)


def inv_mod(x, m):
    assert 1 <= m
    z = inv_gcd(x, m)
    assert z[0] == 1
    return z[1]


def crt(r, m):
    assert len(r) == len(m)
    n = len(r)
    r0 = 0
    m0 = 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue
        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g:
            return (0, 0)
        x = (r1 - r0) // g % u1 * im % u1
        r0 += x * m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return (r0, m0)


def main():
    primes = [4, 9, 5, 7, 11, 13, 17, 19, 23]

    # print(10**9)
    # val = 1
    # for p in primes:
    #     val *= p
    # print(val)

    print(sum(primes))

    offset = 0
    A = []
    for p in primes:
        for i in range(p):
            a = offset + i + 2
            if a == p + offset + 1:
                a = offset + 1
            A.append(a)
        offset += p
    print(*A)

    B = list(map(int, input().split()))
    C = []
    offset = 0
    for p in primes:
        C.append(B[offset] - (offset + 1))
        offset += p
    ans = crt(C, primes)
    print(ans[0])
    

if __name__ == "__main__":
    main()
