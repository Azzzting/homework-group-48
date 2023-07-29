import copy
import hashlib

def GCD(a, b):
    k = a // b
    c = a % b
    while c != 0:
        a = b
        b = c
        k = a // b
        c = a % b
    return b


def xy(a, b):
    if b == 0:
        return 1, 0
    else:
        k = a // b
        c = a % b
        x1, y1 = xy(b, c)
        x, y = y1, x1 - k * y1
    return x, y

def inverse(a, b):
    if b < 0:
        m = abs(b)
    else:
        m = b

    flag = GCD(a, b)
    # 判断最大公约数是否为1，若不是则没有逆元
    if flag == 1:
        x, y = xy(a, b)
        x0 = x % m  
        return x0

    else:
        print("fail!")

def Add(P,Q):
    if P[0] == Q[0]:
        a = (3 * pow(P[0], 2) + a)
        b = (2 * P[1])
        if a % b != 0:
            val = inverse(b, 17)
            y = (a * val) % 17
        else:
            y = (a / b) % 17
    else:
        a = (Q[1] - P[1])
        b = (Q[0] - P[0])
        if a % b != 0:
            val = inverse(b, 17)
            y = (a * val) % 17
        else:
            y = (a / b) % 17

    Rx = (pow(y, 2) - P[0] - Q[0]) % 17
    Ry = (y * (P[0] - Rx) - P[1]) % 17
    return(Rx,Ry)


def mul(n, point):
    if n == 0:
         return 0
    elif n == 1:
        return point

    t = point
    while (n >= 2):
        t = Add(t, point)
        n = n - 1
    return t


def double(point):
    return Add(point,point)


def sign(m, G, d,k):
    e = Hash(m)
    R = mul(k, G)   #R=kg
    r = R[0] % mod_value   
    s = (inverse(k, mod_value) * (e + d * r)) % mod_value
    return r, s

def verify(m, G, r, s, P):
    e = Hash(m)
    w = inverse(s, mod_value)
    e1 = (e * w) % mod_value
    e2 = (r * w) % mod_value
    w = Add(mul(e1, G), mul(e2, P))
    if (w == 0):
        print('false')
        return False
    else:
        if (w[0] % mod_value == r):
            print("签名验证通过")
            return True
        else:
            print('签名不通过')
            return False

def Hash(string):
    s = hashlib.sha256()
    s.update(string.encode())
    b = s.hexdigest()
    return int(b,16)


def deduce_pubkey(s, r, k, G):
    e1=inverse((s+r),17)

    e2=mul(k,G)

    e3=mul(s,G)
    e4=(e3[0],(-e3[1])%17)
    print(e2,e4)

    result=Add(e2,e4)

    print("根据签名推出公钥",result)

mod_value = 19
a = 2
b = 2
G=[7,1]
k=2
message="1234567890"
d=5
r,s=sign(message,G,d,k)
P = mul(d, G)
print("公钥为",P)
verify(message,G,r,s,P)
deduce_pubkey(s,r,k,G)
