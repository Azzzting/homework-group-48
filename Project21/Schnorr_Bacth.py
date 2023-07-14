import hashlib
import random

# 椭圆曲线参数
p = int("fffffffffffffffffffffffffffffffeffffffffffffffff", 16)
a = int("0000000000000000000000000000000000000000000000000000", 16)
b = int("0000000000000000000000000000000000000000000000000007", 16)
Gx = int("3fffffffffffffffffffffffffffffffbce6faada7179e84f3b9cac2fc632551", 16)
Gy = int("37bf51f5cbb6406836bacb8d01554bdae35dbe2181e7a6f788f7e1a8fff0c71d", 16)
n = int("fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141", 16)

def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    if P[0] == Q[0] and P[1] != Q[1]:
        return None
    if P[0] == Q[0]:
        l = (3 * P[0] * P[0] + a) * pow(2 * P[1], p - 2, p) % p
    else:
        l = (Q[1] - P[1]) * pow(Q[0] - P[0], p - 2, p) % p
    x = (l * l - P[0] - Q[0]) % p
    y = (l * (P[0] - x) - P[1]) % p
    return (x, y)

def point_mul(n, P):
    R = None
    for i in range(256):
        if (n >> i) & 1:
            R = point_add(R, P)
        P = point_add(P, P)
    return R

def hash_to_point(msg):
    h = hashlib.sha256()
    h.update(msg)
    digest = h.digest()
    x = int.from_bytes(digest, 'big')
    while True:
        candidate = (x % p, 0)
        if point_mul(n, candidate) is not None:
            return candidate
        x += 1

def sign(msg, sk):
    k = random.randint(1, n-1)
    R = point_mul(k, (Gx, Gy))
    e = int.from_bytes(hashlib.sha256(msg + R[0].to_bytes(32, 'big')).digest(), 'big')
    s = (k - sk * e) % n
    return (R[0], s)

def verify(msg, sig, pk):
    e = int.from_bytes(hashlib.sha256(msg + sig[0].to_bytes(32, 'big')).digest(), 'big')
    R = point_add(point_mul(sig[1], (Gx, Gy)), point_mul(e, pk))
    if R is None or R[0] != sig[0]:
        return False
    return True

# 批量签名
def batch_sign(msgs, sk):
    sigs = []
    for msg in msgs:
        sigs.append(sign(msg, sk))
    return sigs

# 批量验证
def batch_verify(msgs, sigs, pks):
    if len(msgs) != len(sigs) or len(msgs) != len(pks):
        return False
    for i in range(len(msgs)):
        if not verify(msgs[i], sigs[i], pks[i]):
            return False
    return True

# 测试样例
msgs = [b"Message 1", b"Message 2", b"Message 3"]
sk = random.randint(1, n-1)
pk = point_mul(sk, (Gx, Gy))
sigs = batch_sign(msgs, sk)
verified = batch_verify(msgs, sigs, [pk] * len(msgs))

# 输出结果
print("Private Key:", hex(sk))
print("Public Key:", hex(pk[0]))
print("Signatures:")
for i in range(len(msgs)):
    print("- Message:", msgs[i])
    print("  Signature R:", hex(sigs[i][0]))
    print("  Signature s:", hex(sigs[i][1]))
print("Verification Result:", verified)
