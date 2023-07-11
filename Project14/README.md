#### 实验内容：
Implement a PGP scheme with SM2
#### 理论基础：
PGP 使用两种类型的加密算法来保护数据：对称密钥加密和公钥加密。对称密钥加密是一种使用相同密钥加密和解密的算法，因此在加密和解密之间需要共享密钥。而公钥加密则是一种使用不同的密钥加密和解密的算法，其中公钥用于加密，而私钥用于解密。

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project14/img/1.png)
#### 实验思路：
(1)采用SM4以及SM2实现。由sm2_key.py生成SM2的密钥。

(2)用 SM2 签名对称加密算法SM4的密钥。

(3)将加密后的数据和签名作为消息发送给接收方。

(4)接收方根据加密的数据和签名，用 SM2 进行解密和验签操作。最后使用SM4密钥解密信息。

(5)最终得到明文数据。
#### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project14/img/2.png)
#### 实验不足：
实验采取静态方式实现，将在后续学习中对其进行改进，引入TCP/UDP的Client-Server交互式结构。
