import random
import time
from gmssl import sm3, func

def Rho_SM3(n):
    m = hex(random.randint(0, 2**(n+1)-1))[2:] #随即构造m，作为起始seed，用于之后hash
    hash1 = sm3.sm3_hash(func.bytes_to_list(bytes(m, encoding='utf-8')))  #一次hash
    hash2 = sm3.sm3_hash(func.bytes_to_list(bytes(sm3.sm3_hash(func.bytes_to_list(bytes(m, encoding='utf-8'))), encoding='utf-8')))  #两次hash
    cnt = 1
    while hash1[:int(n/4)] != hash2[:int(n/4)]:  #不断进行hash，寻找碰撞
        cnt += 1
        hash1 = sm3.sm3_hash(func.bytes_to_list(bytes(hash1, encoding='utf-8')))
        hash2 = sm3.sm3_hash(func.bytes_to_list(bytes(sm3.sm3_hash(func.bytes_to_list(bytes(hash2, encoding='utf-8'))), encoding='utf-8')))
    for j in range(cnt):  #得到结果并返回
        if sm3.sm3_hash(func.bytes_to_list(bytes(hash1, encoding='utf-8')))[:int(n/4)] == sm3.sm3_hash(func.bytes_to_list(bytes(hash2, encoding='utf-8')))[:int(n/4)]:
            return [hash1, hash2,sm3.sm3_hash(func.bytes_to_list(bytes(hash1, encoding='utf-8')))[:int(n/4)]]
        else:
            hash1 = sm3.sm3_hash(func.bytes_to_list(bytes(hash1, encoding='utf-8')))
            hash2 = sm3.sm3_hash(func.bytes_to_list(bytes(hash2, encoding='utf-8')))


if __name__ == '__main__':
    n=16#攻击bit数
    print("攻击bit数为：",n)
    start = time.time()
    res=Rho_SM3(n)
    end=time.time()
    print("消息1:", res[0])
    print("消息2:", res[1])
    print("结果:", res[2])
    print(end-start,"seconds\n")
