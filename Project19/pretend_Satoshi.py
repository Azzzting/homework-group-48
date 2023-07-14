import random
from gmssl import sm3
from hashlib import sha1


p=0x8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3
a=0x787968B4FA32C3FD2417842E73BBFEFF2F3C848B6831D7E0EC65228B3937E498

b=0x63E4C6D3B23B0C849CF84241484BFE48F61D59A5B16BA06E6E12D1DA27C5249A
n=0x8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7
Gx=0x421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D
Gy=0x0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2



def XGCD(a, b):
    if (b == 0):
        return 1, 0, a
    else:
        x, y, d = XGCD(b, a % b)
        return y, (x - (a // b) * y), d


def get_inverse(a, b):
    return XGCD(a, b)[0] % b


# 求最大公约数——用于约分化简
def get_gcd(x, y):
    if y == 0:
        return x
    else:
        return get_gcd(y, x % y)

    # 计算P+Q函数


def calculate_p_q(x1, y1, x2, y2, a, b, p):
    flag = 1  # 控制符号位

    # 若P = Q，则k=[(3x1^2+a)/2y1]mod p
    if x1 == x2 and y1 == y2:
        member = 3 * (x1 ** 2) + a  # 计算分子
        denominator = 2 * y1  # 计算分母

    # 若P≠Q，则k=(y2-y1)/(x2-x1) mod p
    else:
        member = y2 - y1
        denominator = x2 - x1
        if member * denominator < 0:
            flag = 0
            member = abs(member)
            denominator = abs(denominator)

    # 将分子和分母化为最简
    gcd_value = get_gcd(member, denominator)
    member = member // gcd_value
    denominator = denominator // gcd_value

    # 求分母的逆元
    inverse_value = get_inverse(denominator, p)
    k = (member * inverse_value)
    if flag == 0:
        k = -k
    k = k % p

    # 计算x3,y3
    x3 = (k ** 2 - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    return [x3, y3]


# 计算2P函数
def calculate_2p(p_x, p_y, a, b, p):
    tem_x = p_x
    tem_y = p_y
    p_value = calculate_p_q(tem_x, tem_y, p_x, p_y, a, b, p)
    tem_x = p_value[0]
    tem_y = p_value[1]
    return p_value


# 计算nP函数
def calculate_np(p_x, p_y, n, a, b, p):
    p_value = ["0", "0"]
    p_temp = [0, 0]
    while n != 0:
        if n & 1:
            if (p_value[0] == "0" and p_value[1] == "0"):
                p_value[0], p_value[1] = p_x, p_y
            else:
                p_value = calculate_p_q(p_value[0], p_value[1], p_x, p_y, a, b, p)
        n >>= 1
        p_temp = calculate_2p(p_x, p_y, a, b, p)
        p_x, p_y = p_temp[0], p_temp[1]
    return p_value


def get_key():
    dA=random.randrange(0,n)
    PA=calculate_np(Gx, Gy, dA, a, b, p)
    return dA,PA

def get_bitsize(num):
    len=0
    while num/256:
        len+=1
        num=int (num/256)
    return len


msg="1234567890"

def ECDSA():
    PA=[0,0]
    def ECDSA_sign(msg):
        nonlocal  PA
        M = msg.encode()
        dA, PA = get_key()
        k = random.randrange(1, n)
        R = calculate_np(Gx, Gy, k, a, b, p)
        r = R[0] % n
        e = int(sha1(M).hexdigest(), 16)
        s = (get_inverse(k, n) * (e + dA * r)) % n
        print(PA)
        print(r,s)
        print(e)
        return r, s

    def ECDSA_verif_sign(msg, sign):
        r, s = sign
        M = msg.encode()
        e = int(sha1(M).hexdigest(), 16)
        w = get_inverse(s, n)
        temp1 = calculate_np(Gx, Gy, e * w, a, b, p)
        temp2 = calculate_np(PA[0], PA[1], r * w, a, b, p)
        R, S = calculate_p_q(temp1[0], temp1[1], temp2[0], temp2[1], a, b, p)
        if (r == R):
            return True
        else:
            return False
    return ECDSA_verif_sign(msg,ECDSA_sign(msg))

P=[26877259512020005462763638353364532382639391845761963173968516804546337027093, 48566944205781153898153509065115980357578581414964392335433501542694784316391]
r,s=41159732757593917641705955129814776632782548295209210156195240041086117167123, 57859546964026281203981084782644312411948733933855404654835874846733002636486
def forge_ECDSA():
    def forge_sign():
        u = random.randrange(1, n)
        v = random.randrange(1, n)
        temp1 = calculate_np(Gx, Gy, u, a, b, p)
        temp2 = calculate_np(P[0], P[1], v, a, b, p)
        R = x, y = calculate_p_q(temp1[0], temp1[1], temp2[0], temp2[1], a, b, p)
        f_r = x % n
        f_e = (f_r * u * get_inverse(v, n)) % n
        f_s = (f_r * get_inverse(v, n)) % n
        return f_r, f_s, f_e

    r,s,e=forge_sign()
    print("伪造的签名为：")
    print(r,s)

    def verify(r,s,e):
        w = get_inverse(s, n)
        temp1 = calculate_np(Gx, Gy, e * w, a, b, p)
        temp2 = calculate_np(P[0], P[1], r * w, a, b, p)
        R, S = calculate_p_q(temp1[0], temp1[1], temp2[0], temp2[1], a, b, p)
        if (r == R):
            return True
        else:
            return False
    return verify(r,s,e)

print(forge_ECDSA())
