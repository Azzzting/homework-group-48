# 客户端
import socket
from gmssl import sm2, sm4
import sys
import random

p = 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF'
a = 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC'
b = '28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93'
n = 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123'
g = '32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7BC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0'

# 返回u mod v的倒数。
def inverse(u, v):
    u3, v3 = u, v
    u1, v1 = 1, 0
    while v3 > 0:
        q = divmod(u3, v3)[0]
        u1, v1 = v1, u1 - v1 * q
        u3, v3 = v3, u3 - v3 * q
    while u1 < 0:
        u1 = u1 + v
    return u1

def generate_d2():
    i = int(n, 16)
    d1 = random.randint(1, i - 1)
    return d1

# 产生-G，实现椭圆曲线减法
def generate_G_1(G):
    sm2_c = sm2.CryptSM2(private_key="", public_key="")
    leng = len(G)
    xg = G[0:sm2_c.para_len]
    yg = G[sm2_c.para_len:leng]
    yg = int(yg, 16)
    yg = (-yg) % int(p, 16)
    yg = hex(yg)[2:]
    G_1 = xg + yg
    return G_1

# 生成公钥
def generate_P(d2, P1):
    i = int(n, 16)
    sm2_c = sm2.CryptSM2(private_key="", public_key="")
    temp = sm2_c._kg(inverse(d2, i), P1)
    G_1 = generate_G_1(g)  # -G
    P = sm2_c._add_point(temp, G_1)  # 两个点相加
    P = sm2_c._convert_jacb_to_nor(P)  # 得到最终的x||y
    return P

def generate_r_s2_s3(d2, Q1, e):
    i = int(n, 16)
    sm2_c = sm2.CryptSM2(private_key="", public_key="")
    k2 = generate_d2()
    Q2 = sm2_c._kg(k2, g)
    k3 = generate_d2()
    temp = sm2_c._kg(k3, Q1)
    P = sm2_c._add_point(temp, Q2)  # 两个点相加
    P = sm2_c._convert_jacb_to_nor(P)  # 得到最终的x||y
    x1 = int(P[0:sm2_c.para_len], 16)
    r = (x1 + int(e.hex(), 16)) % i
    s2 = (d2 * k3) % i
    s3 = d2 * (r + k2) % i
    return r, s2, s3

# 建立TCP连接
HOST = 'localhost'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connected to', HOST, 'on port', PORT)

# 发送P1
P1 = input("请输入P1: ")
s.sendall(P1.encode('utf-8'))
response = s.recv(1024).decode('utf-8')
print(response)

# 发送Q1
Q1 = input("请输入Q1: ")
s.sendall(Q1.encode('utf-8'))
response = s.recv(1024).decode('utf-8')
print(response)

# 发送e
e = input("请输入e: ")
s.sendall(bytes.fromhex(e))
response = s.recv(1024).decode('utf-8')
print(response)

# 接收r
r = s.recv(1024).decode('utf-8')
print("接收的r", r)
s.sendall("OK".encode('utf-8'))

# 接收s2
s2 = s.recv(1024).decode('utf-8')
print("接收的s2", s2)
s.sendall("OK".encode('utf-8'))

# 接收s3
s3 = s.recv(1024).decode('utf-8')
print("接收的s3", s3)
s.sendall("OK".encode('utf-8'))

s.close()
