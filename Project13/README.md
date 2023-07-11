#### 实验内容：
Implement the above ECMH scheme
#### 理论基础：
ECMH即把哈希映射成椭圆曲线上的点，然后利用ECC的加法对其进行操作。

为达到相同的安全性，ECMH算法需要的密钥长度远远小于哈希求和算法，因而ECMH相较哈希求和算法更为安全。（图源网络）

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project13/img/3.png)

#### 实验思路：
(1)首先先对消息进行hash。

(2)开始遍历从零到正无穷，并补充在hash之前得到hash2，对hash2做hash。

(3)令得到的hash值模p赋值给x。

(4)根据求二次剩余的算法得到y，如果有y就跳转到5，如果没有y就到2。

(5)由于二次剩余得到的y有两个，那么这样选择两个y中的一个，根据消息的编码，如果最后以个数字为0，选小一点的y，如果为1，选大一点的y。
#### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project13/img/2.png)
#### 实验不足：
本次实现仅实现了求并集和交集，且由于算法较原始，未进行优化导致算法运行时间较长。将在后续的学习中对其进行优化提升性能和完善功能。