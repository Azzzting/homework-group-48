### 实验内容：
Implement the above ECMH scheme
### 理论基础：
ECMH是指基于椭圆曲线的移动哈希(Moving Hash)算法，用于在椭圆曲线数字签名(ECDSA)中生成随机数k。其理论依据如下：

在ECDSA中，随机数k的选择对安全性至关重要，如果k被猜测出来，则可以轻易地计算出私钥d。因此，为了保证安全性，k必须是随机的且只使用一次。

传统的随机数生成方法，如伪随机数生成器(PRNG)或硬件随机数生成器(HRNG)，存在一定的弱点，例如PRNG可能受到预测攻击，HRNG可能受到物理攻击。

ECMH利用移动哈希函数来生成随机数k，移动哈希是指将消息m和一个初始值h作为输入，然后通过哈希函数计算出一个输出h1，并将h1作为下一次的输入，重复该过程直到得到所需的输出。在ECMH中，初始值h是由一些公共信息和私有信息共同生成的，因此可以保证k的随机性和不可预测性。

ECMH的理论依据是基于椭圆曲线上的离散对数问题，该问题是计算y = g^x (mod p)中x的值，已知g、y和p。椭圆曲线上的离散对数问题比传统RSA等密码学算法更难以破解，因此ECMH可以提供更高的安全性。。

在达到相同安全性的同时，ECMH算法需要的密钥长度远远小于哈希求和算法，因而ECMH相较哈希求和算法更为安全。

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project13/img/3.png)

### 实验思路：
#### 完成相关函数的编写：
##### 求逆函数：
```python
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
def EC_inv(p):
    r = [p[0]]
    r.append(P - p[1])
    return r
```
##### 加法函数：
```python
def add(ecmh, msg):
    dot = trans(msg)
    tmp = EC_add(ecmh, dot)
    return tmp
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
```
##### 减法函数：
```python
def EC_sub(p, q):
    q_inv = EC_inv(q)
    return EC_add(p, q_inv)
```
##### 映射函数：
```python
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
```
#### 总体思路概括：
    (1)定义椭圆曲线的参数(A, B, P, N)，其中P为一个大素数，N为椭圆曲线上点的个数。
    (2)定义哈希函数(SHA256)和随机数生成器，用于将消息映射到椭圆曲线上的点并生成随机数k。
    (3)定义椭圆曲线加法(EC_add)、椭圆曲线倍乘(EC_double)、椭圆曲线点求逆(EC_inv)和椭圆曲线点相减(EC_sub)等操作，用于实现ECMH算法。
    (4)实现trans、add、single和combine函数，分别用于将消息映射到椭圆曲线上的点、计算单个消息的签名、计算多个消息的签名并返回它们的并集和交集。
    (5)给出两个消息的签名以及它们的并集和交集。
### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project13/img/2.png)
### 实验不足：
本次实现仅实现了求并集和交集，且由于算法较原始，未进行优化导致算法运行时间较长。将在后续的学习中对其进行优化提升性能和完善功能。
