import copy
import hashlib
def gcd(a, b):
    k = a // b
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        k = a // b
        remainder = a % b
    return b


def get_xy(a, b):
    if b == 0:
        return 1, 0
    else:
        k = a // b
        remainder = a % b
        x1, y1 = get_xy(b, remainder)
        x, y = y1, x1 - k * y1
    return x, y


def inverse(a, b):
    if b < 0:
        m = abs(b)
    else:
        m = b

    flag = gcd(a, b)
    if flag == 1:
        x, y = get_xy(a, b)
        x0 = x % m  
        return x0

    else:
        print("Do not have!")

### y^2=x^3+ax+by mod (mod_value)
def add(P,Q):
    if P[0] == Q[0]:
        b = (3 * pow(P[0], 2) + a)
        c = (2 * P[1])
        if b % c != 0:
            val = inverse(c, 17)
            y = (b * val) % 17
        else:
            y = (b / c) % 17
    else:
        b = (Q[1] - P[1])
        c = (Q[0] - P[0])
        if b % c != 0:
            val = inverse(c, 17)
            y = (b * val) % 17
        else:
            y = (b / c) % 17

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
        t = add(t, point)
        n = n - 1
    return t


def double(point):
    return add(point,point)



def sign(m, G, d,k):
    e = Hash(m)
    R = mul(k, G)  
    r = R[0] % mod_value
    s = (inverse(k, mod_value) * (e + d * r)) % mod_value
    return r, s

def verify(m, G, r, s, P):
    e = Hash(m)
    w = inverse(s, mod_value)
    ele1 = (e * w) % mod_value
    ele2 = (r * w) % mod_value
    w = add(mul(ele1, G), mul(ele2, P))
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
    ele1=inverse((s+r),17)

    ele2=mul(k,G)

    ele3=mul(s,G)
    ele4=(ele3[0],(-ele3[1])%17)
    print(ele2,ele4)

    result=add(ele2,ele4)

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
