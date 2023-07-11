import socket
import json
from SM2__ import *
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
HOST=""
PORT=5087
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
print('目前监听的端口号是：',PORT)
print("可以发送消息")
while True:
    sm2_B = SM2(ID='Bob')
    data0,addr=s.recvfrom(1024)
    #print("T1[0]:",data0.decode("utf8","ignore"))
    c=("接收成功!")
    s.sendto(c.encode(),addr)
    
    data1,addr=s.recvfrom(1024)
    #print("T1[1]:",data1.decode())
    
    c=("信息1接收成功")
    s.sendto(c.encode(),addr)
    T1=(int(data0.decode()),int(data1.decode()))
    T2=sm2_B.multiply(get_inverse(sm2_B.sk,sm2_B.n),T1)
    print("发送信息为：",T2)
    T2=list(T2)
    s.sendto(str(T2[0]).encode(),addr)
    data,addr=s.recvfrom(1024)
    print(data.decode())
    
    s.sendto(str(T2[1]).encode(),addr)
    data,addr=s.recvfrom(1024)
    print(data.decode())
    break

    
s.close()
