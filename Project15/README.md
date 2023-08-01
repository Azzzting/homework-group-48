### 实验内容：
implement sm2 2P sign with real network communication
### 理论基础：
SM2 2P签名协议是一种允许双方使用SM2椭圆曲线公钥加密算法对消息进行安全签名的加密协议。该协议的基本思想是双方交换消息以建立共享密钥，然后使用该密钥对消息进行签名。

该协议可以通过以下步骤来实现:

    (1)双方都生成自己的SM2公钥和私钥。
    (2)A将其公钥发送给B。
    (3)B生成一个随机数，并使用该随机数与A的公钥计算共享密钥。
    (4)B将共享秘密发送给A。
    (5)A生成一个随机数，并使用该随机数与B的公钥计算共享密钥。
    (6)A将共享秘密发送给B。
    (7)双方都使用这两个共享秘密来派生对称加密密钥。
    (8)A使用自己的私钥对信息进行签名，发送给B。
    (9)B使用A的公钥验证签名。
课堂PPT截图：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project15/img/1.png)
### 实验思路：
按上述流程实现的各部分伪代码如下：
##### 生成公私钥并发送
```python
A_private_key, A_public_key = SM2_generate_key()
B_private_key, B_public_key = SM2_generate_key()

send(B_public_key)
```
##### 生成共享密码并发送
```python
B_public_key = receive()
shared_secret_B = SM2_compute_shared_secret(B_private_key, B_public_key)

send(shared_secret_B)
```
##### 生成对称密钥并签名
```python
shared_secret_A = receive()
encryption_key = SM2_derive_encryption_key(shared_secret_A, shared_secret_B)

signature = SM2_sign(A_private_key, message)
encrypted_message = AES_encrypt(message, encryption_key)
send(encrypted_message, signature)
```
##### 收到信息并验证签名
```python
encrypted_message, signature = receive()
message = AES_decrypt(encrypted_message, encryption_key)
if SM2_verify(B_public_key, message, signature):
    // Signature is valid
else:
    // Signature is invalid
```
结合上述步骤，具体可以按以下流程进行分步实现：

    (1)初始化签名方和验证方的参数，包括生成椭圆曲线的基点、阶数以及各自的私钥和随机数。
    (2)生成签名方的公钥，并输出私钥。
    (3)通过验证方私钥和签名方公钥生成验证方的公钥，并输出私钥。
    (4)定义待签名的消息和附加信息。
    (5)生成签名方的临时公钥和消息摘要。
    (6)根据验证方私钥、随机数、临时公钥和消息摘要生成签名。
    (7)验证生成的签名是否有效，输出验证结果。
### 实验结果：
#### 本实验实现了两个版本的2P。

##### 无网络环境版本：

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project15/img/2.png)

##### 增加网络环境,加入socket编程版本：

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project15/img/3.png)
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project15/img/4.png)
### 实验不足：
缺少网络环境测试等相关功能，会在后续的学习中继续补充。

