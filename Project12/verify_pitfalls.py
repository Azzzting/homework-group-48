from numpy import *
import random
from Cryptodome.Util.number import * 
import hashlib
import ecdsa
import math
# y ^ 2 = x ^ 3 + a * x + b (mod p)
a = 2
b = 3
p = 233

def ECC_add(P, Q):
    flag = 1
    if P == 0 :
        return Q
    if Q == 0:
        return P
    if (P == Q):
        d = ((3 * (P[0] ** 2) + a ) * inverse(2 * P[1], p)) % p
    else:
        b = Q[1] - P[1]
        c = Q[0] - P[0]
        if b * c < 0:
            flag = 0
            b = abs(b)
            c = abs(c)
        gcd_value = gcd(b, c)
        b = b // gcd_value
        c = c // gcd_value
        d = (b * inverse(c, p))
        if flag == 0:
            d = -d
        a = a % p
    x = (d ** 2 - P[0] - Q[0]) % p
    y = (d * (P[0] - x) - P[1]) % p
    return [x,y]

def add(P, Q):
        if not P:
            return Q
        if not Q:
            return P
        if P[0] == Q[0]:
            if (P[1] + Q[1]) % p == 0:
                return
            c = (3 * P[0] * Q[0] + a) * \
                pow(int(P[1] + Q[1]), p - 2, p) % p
        else:
            c = (Q[1] - P[1]) * pow(int(Q[0] - P[0]), p - 2, p) % p
        x = (c * c - P[0] - Q[0]) % p
        y = (c * (P[0] - x) - P[1]) % p
        return x, y
    
def mult(n, P):
        if n == 0:
            return
        Q = mult(n >> 1, P)
        return add(add(Q, Q), P) if n & 1 else add(Q, Q)
    


def Sign(d, e, n, G):
    while 1:
        k = random.randint(1, n)
        R = mult(k, G)
        r = R[0] % n
        s = (inverse(k, n) * (e + d * r)) % n
        if s == 0 or r == 0:
            continue
        else:
            break
    return [r, s]

def Sign_k(k, d, e, n, G):
    R = mult(k, G)
    r = R[0] % n
    if r == 0:
        print("r can't be 0, choose the new k")
        return
    s = (inverse(k, n) * (e + d * r)) % n
    if s == 0:
        print("s can't be 0, choose the new k")
        return
    return [r, s]

def Verify(P, e, n, G, r, s):  #e = hash(m)
    w = inverse(s, n) % n
    t1 = (e * w) % n
    t2 = (r * w) % n
    X = add(mult(t1, G), mult(t2, P))
    if X == None:
        print("the sig invalid")
        return
    else:
        r_ = X[0] % n
    if r == r_:
        return 1
    else:
        return 0

def know_k(k, G, P, n, e, r, s):
    d = ((s * k - e) * inverse(r, n)) % n
    return d

def reknow_k(k1, k2, G, P, n, e1, e2, r1, s1, r2, s2):
    r = r1
    d = ((e1 * s2 - s1 * e2) * inverse(s1 * r - r * s2, n)) % n
    return d

def same_k(k, G, P, n, d2, e1, e2, r1, s1, r2, s2):
    r = r1
    d1 = (inverse(s2 * r, n) * (s1 * e2 - s2 * e1 + s1 * r * d2)) % n
    return d1


def pretend(G, P, n):
    u = random.randint(1, n)
    v = random.randint(1, n)
    R = add(mult(u, G), mult(v, P))
    if R == 0:
        r = 0
    else:
        r = R[0] % n
    e = (r * u * inverse(v, n)) % n
    s = (r * inverse(v, n)) % n
    return e, r, s

def get_order(x0, y0): # copied by CSDN

    x1 = x0
    y1 = (-1 * y0) % p
    temp_x = x0
    temp_y = y0
    n = 1
    while True:
        n += 1
        p_value = add([temp_x,temp_y], [x0, y0])
        if p_value[0] == x1 and p_value[1] == y1:
            return n+1
        temp_x = p_value[0]
        temp_y = p_value[1]

if __name__ == '__main__':
    print("基本信息如下：")
    m = '01234567890'
    G = [141, 41]
    n = get_order(G[0], G[1])
    print("n = ", n)
    d = 3
    P = mult(d, G)
    e = int(hashlib.sha256(str(m).encode()).hexdigest(),base = 16) % n
    print("e = ", e)
    S = Sign(d, e, n, G)
    r = S[0]
    s = S[1]
    print("m = '{}'".format(m))
    print("d = ", d)
    print("--------------------------------")
    print("使用ECDSA进行签名并验证：")
    print("ECDSA sign : ",S)
    if Verify(P, e, n, G, r, s) == 1:
        print("TRUE！")
    print("--------------------------------")
    print("进行伪造：")
    e_, r_, s_ = pretend(G, P, n)
    print("伪造签名信息如下: hash(m') = {}", "r' = {}"," s' = {}".format(e_, r_, s_))
    if Verify(P, e_, n, G, r_, s_) == 1:
        print("伪造TRUE！")
    print("--------------------------------")
    k = 3
    print("k = ", k)
    S = Sign_k(k, d, e, n, G)
    r = S[0]
    s = S[1]
    print("m: '{}' 的签名为： {}".format(m, S))
    print("下面验证已知k可以得到私钥d:")
    d_ = know_k(k, G, P, n, e, r, s)
    print(d)
    print("d = ", d_)
    if d_ == d:
        print("TRUE！")
    print("下面验证使用相同的k可以获得私钥d:")
    m2 = '9876543210'
    e2 = int(hashlib.sha256(str(m2).encode()).hexdigest(),base = 16)
    S2 = Sign_k(k, d, e2, n, G)
    r2 = S2[0]
    s2 = S2[1]
    print("m1 = '{}'".format(m))
    print("m2 = '{}'".format(m2))
    print("k = ", k)
    print("d = ", d)
    print("ECDSA sign1 : ",S)
    print("ECDSA sign2 : ",S2)
    d__ = reknow_k(k, k, G, P, n, e, e2, r, s, r2, s2)
    print("d = ", d__)
    if d__ == d:
        print("True")
    print("--------------------------------")
    print("下面验证两个使用者使用相同k可以获得私钥d:")
    d2 = 7
    S3 = Sign_k(k, d2, e2, n, G)
    r3 = S3[0]
    s3 = S3[1]
    print("m1 = '{}'".format(m))
    print("m2 = '{}'".format(m2))
    print("k = ", k)
    print("unknown d1 = ", d)
    print("d2 = ", d2)
    print("ECDSA sign1 : ",S)
    print("ECDSA sign2 : ",S3)
    d___ = same_k(k, G, P, n, d2, e, e2, r, s, r3, s3)
    print("cal d1 = ", d___)
    if(d___ == d):
        print("TRUE！")
    print("--------------------------------")
    print("----下面验证：(r,s) and (r,-s) 均是可靠签名：")
    print("one sign is : ", S)
    anotherS = [S[0], -S[1]]
    print("another sign is : ", anotherS)
    if Verify(P, e, n, G, anotherS[0], anotherS[1]) == 1:
        print("another sign {} vrfy pass.".format(anotherS))
