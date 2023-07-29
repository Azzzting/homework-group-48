from hashlib import sha256
from random import randint
from math import sqrt

A = 0
B = 7
P = 115792089237316195423570985008687907853269984665640564039457584007908834671663
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337


def SHA256(s):
    msg = s
    return sha256(bytes(bytearray(msg, encoding='utf-8'))).hexdigest()


def inv(a, n):
    def gcd(a, b, arr):
        if b == 0:
            arr[0] = 1
            arr[1] = 0
            return a
        c = gcd(b, a%b, arr)
        t = arr[0]
        arr[0] = arr[1]
        arr[1] = t-int(a/b)*arr[1]
        return c
    arr = [0,1,]
    gcd = gcd(a, n, arr)
    if gcd == 1:
        return (arr[0]%n+n)%n
    else:
        return -1

def EC_add(p, q):  
    if p == 0 and q == 0: return 0  # 0 + 0 = 0
    elif p == 0: return q  # 0 + q = q
    elif q == 0: return p  # p + 0 = p
    else:
        if p[0] == q[0]:  
            if (p[1] + q[1]) % P == 0: return 0  # mutually inverse
            elif p[1] == q[1]: return EC_double(p)
        elif p[0] > q[0]: 
            tmp = p
            p = q
            q = tmp
        r = []
        s = (q[1] - p[1]) * inv(q[0] - p[0], P) % P  # 斜率
        r.append((s ** 2 - p[0] - q[0]) % P)
        r.append((s * (p[0] - r[0])- p[1]) % P)
        return (r[0], r[1])

def EC_inv(p):
    r = [p[0]]
    r.append(P - p[1])
    return r

def EC_sub(p, q):
    q_inv = EC_inv(q)
    return EC_add(p, q_inv)


def EC_double(p):
    r = []
    s = (3 * p[0] ** 2 + A) * inv(2 * p[1], P) % P
    r.append((s ** 2 - 2 * p[0]) % P)
    r.append((s * (p[0] - r[0]) - p[1]) % P)
    return (r[0], r[1])


def trans(msg): # 映射到椭圆曲线上的点
    def Legendre(y,p): 
        return pow(y,(p - 1) // 2,p)
    def msg_to_x(m):
        m = SHA256(m)
        while 1:  # cycle until x belong to QR
            x = int(m, 16)
            if Legendre(x, P):
                break
            m = SHA256(m)
        return x
    def get_y(x):  # y^2 = x^3 + 7 mod P
        right = (x ** 3 + 7) % P
        while 1:
            a = randint(0, P)
            if Legendre(a, P) == -1:
                break
        b = int(a + sqrt(a ** 2 - right))
        e = (P + 1) // 2
        y = pow(b, e, P)
        return y
    x = msg_to_x(msg)
    y = get_y(x)
    return (x, y)


def add(ecmh, msg):
    dot = trans(msg)
    tmp = EC_add(ecmh, dot)
    return tmp

def single(msg):
    return add(0, msg)

def combine(msg_set):
    ans = single(msg_set[0])
    num = len(msg_set) - 1
    for i in range(num):
        ans = add(ans, msg_set[i+1])
    return ans

if __name__=="__main__":
    m1 = "0123456789"
    m2 = "0123456789"

    print('m1签名:', single(m1))
    print('m2签名:', single(m2))
    print('并集为：', combine([single(m1),single(m2)]))
    print('交集为：', add(single(m1), single(m2))
