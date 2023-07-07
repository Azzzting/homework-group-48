import random
import time
from gmssl import sm3, func

#构造随机消息空间
m = str(random.random())
length = len(m)
hash = sm3.sm3_hash(func.bytes_to_list(bytes(m, encoding='utf-8')))

#攻击函数（bit_num:攻击长度）
def Birthday_attack(bit_num):
    num = int(2 ** (bit_num / 2))
    ans = [-1] * 2**bit_num
    #循环遍历
    for i in range(num):
        temp = int(hash[0:int(bit_num / 4)], 16)
        if ans[temp] == -1:
            ans[temp] = i
        else:
            return hex(temp)

if __name__ == '__main__':
    bit_num = 32#选择碰撞的bit长度
    start = time.time()
    res = Birthday_attack(bit_num)
    end = time.time()
    print("前",bit_num,"位碰撞为{}".format(res))
    print(end- start,'seconds\n')
