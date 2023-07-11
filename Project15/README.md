#### 实验内容：
implement sm2 2P sign with real network communication
#### 理论基础：
PGP 使用两种类型的加密算法来保护数据：对称密钥加密和公钥加密。

PGP将对称密钥加密，并使用接收方的公钥进行加密。这种方式可以保证密钥的安全性，同时可以确保只有接收方可以解密对称密钥，从而保护了数据的机密性。接收方使用自己的私钥对加密的对称密钥进行解密，然后使用对称密钥对数据进行解密。这种方式既可以保护数据的安全性，也可以提高加解密的速度。

为数据通信提供加密隐私和身份验证。PGP 用于对文本、电子邮件、文件、目录和整个磁盘分区进行签名、加密和解密，并提高电子邮件通信的安全性。

课堂PPT截图：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project15/img/1.png)
#### 实验思路：
按以下流程进行分步实现：

(1)初始化签名方和验证方的参数，包括生成椭圆曲线的基点、阶数以及各自的私钥和随机数。

(2)生成签名方的公钥，并输出私钥。

(3)通过验证方私钥和签名方公钥生成验证方的公钥，并输出私钥。

(4)定义待签名的消息和附加信息。

(5)生成签名方的临时公钥和消息摘要。

(6)根据验证方私钥、随机数、临时公钥和消息摘要生成签名。

(7)验证生成的签名是否有效，输出验证结果。
#### 实验结果：
本实验实现了两个版本的2P。

无网络环境版本：

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project15/img/2.png)

增加网络环境,加入socket编程版本：

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project15/img/3.png)
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project15/img/4.png)
#### 实验不足：
缺少网络环境测试等相关功能，会在后续的学习中继续补充。

