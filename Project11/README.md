#### 实验内容：
impl sm2 with RFC6979
#### 理论依据：
签名流程：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project11/img/2.png)

验证流程：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project11/img/3.png)
#### 实验思路：
基于椭圆曲线算法，在椭圆曲线里面k值(用于签名)是要严格保密的，所以利用RFC6979（确定性签名算法）来生成k

(1)利用RFC4979，计算椭圆曲线上的点，生成随机数k.

(2)借助私钥和公钥进行加解密.

(3)对比加解密结果.
#### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project11/img/1.png)
