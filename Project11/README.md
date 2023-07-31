### 实验内容：
impl sm2 with RFC6979
### 理论依据：
#### RFC6979：
算法是一种确定性的 ECDSA 签名算法，它可以在不使用伪随机数生成器的情况下生成安全的随机数。RFC6979 算法的核心思想是使用哈希函数和椭圆曲线上的点来计算随机数，从而避免了使用伪随机数生成器可能引入的安全漏洞。

RFC6979 算法的具体步骤如下：

    (1)计算消息的哈希值。
    (2)将私钥和哈希值拼接成一个字符串，并使用哈希函数计算哈希值。
    (3)将哈希值转换为一个整数，并将其作为种子。
    (4)使用种子和椭圆曲线参数计算椭圆曲线上的点 H。
    (5)将 H 的 x 坐标转换为一个整数，并将其作为随机数的候选值。
    (6)如果候选值大于等于椭圆曲线上的点数 n，则重新计算 H 并重复步骤 5。
    (7)如果候选值小于椭圆曲线上的点数 n，则将其作为随机数。
PPT中的叙述：

签名流程：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project11/img/2.png)

验证流程：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project11/img/3.png)
### 实验思路：
#### 关键步骤的伪代码实现：
##### 定义 SM2 椭圆曲线参数及hash函数
```python
p ，a ，b，n
# 定义哈希函数
def hash_function(message):
    # 使用 SM3 哈希算法计算消息的哈希值
    hash_value = sm3_hash(message)
    return hash_value
```
##### 定义签名函数
```python
def sign_with_rfc6979(private_key, message):
    # 计算消息的哈希值
    hash_value = hash_function(message)
    # 使用 RFC6979 算法生成 k 值
    k = rfc6979(private_key, hash_value)
    # 计算椭圆曲线上的点 R
    R = k * G
    # 计算 e 值
    e = int.from_bytes(hash_value, byteorder='big')
    # 计算 s 值
    s = (e + private_key * R.x) * inv(k + 1, n) % n
    # 返回签名结果
    return R, s
```
```python
# 定义验证函数
def verify(public_key, message, signature):
    # 从签名中提取 R 和 s 值
    R, s = signature
    # 计算消息的哈希值
    hash_value = hash_function(message)
    # 计算 e 值
    e = int.from_bytes(hash_value, byteorder='big')
    # 计算椭圆曲线上的点 T
    T = e * G + s * public_key
    # 验证签名是否正确
    return R.x == T.x % p % n
```
根据伪代码实现及PPT讲述，概括可得总体思路：

    基于椭圆曲线算法，在椭圆曲线里面k值(用于签名)是要严格保密的，所以利用RFC6979（确定性签名算法）来生成k

    (1)利用RFC6979，计算椭圆曲线上的点，生成随机数k.

    (2)借助私钥和公钥进行加解密.

    (3)对比加解密结果.
### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project11/img/1.png)
