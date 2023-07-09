#### 实验内容：
verify the above pitfalls with proof-of-concept code
#### 理论基础：
主要分为两个阶段：签名阶段与验证阶段。

签名过程如下：

(1)选择一条椭圆曲线Ep(a,b)，和基点G；

(2)选择私有密钥k（k<n，n为G的阶），利用基点G计算公开密钥K=kG；

(3)产生一个随机整数r（r<n），计算点R=rG；

(4)将原数据和点R的坐标值x,y作为参数，计算SHA1做为hash，即Hash=SHA1(原数据,x,y)；

(5)计算s≡r - Hash * k (mod n)

(6)r和s做为签名值，如果r和s其中一个为0，重新从第3步开始执行

验证过程如下：

(1)接受方在收到消息(m)和签名值(r,s)后，进行以下运算

(2)计算：sG+H(m)P=(x1,y1), r1≡ x1 mod p。

(3)验证等式：r1 ≡ r mod p。

(4)如果等式成立，接受签名，否则签名无效。
#### 实验思路：
在实现中可以发现，ECDSA的实现步骤类似于我们之前学习的RSA数字签名算法

(1)初始化化秘钥组，生成ECDSA算法的公钥和私钥

(2)执行私钥签名， 使用私钥签名，生成私钥签名

(3)执行公钥签名，生成公钥签名

(4)使用公钥验证私钥签名。遵从的原则就是“私钥签名、公钥验证”。
#### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project12/img/1.png)
