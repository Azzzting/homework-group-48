#### 实验内容：
report on the application of this deduce technique in Ethereum with ECDSA
#### 理论基础：
一、密钥生成

(1)选择一条椭圆曲线E_P(a,b)，选择基点G，G的阶数为n
  
(2)选择随机数d ∈n为私钥，计算公钥Q = d⋅G

二、签名

(1)对消息m使用消息摘要算法，得到z=hash(m)

(2)生成随机数k∈n，计算点(x, y)=k⋅G

(3)取r=x mod n，若r=0则重新选择随机数k

(4)计算s = k^−1(z+rd) mod n，若s=0则重新选择随机数k

(5)上述(r,s)即为ECDSA签名

三、验证

使用公钥Q和消息m，对签名(r,s)进行验证。

(1)验证r,s∈n

(2)计算z = hash(m)

(3)计算u_1 =zs^−1 mod n和u_2 = rs^−1 mod n

(4)计算(x, y) = u1⋅G+u2⋅Q mod n

(5)判断r == x，若相等则签名验证成功

四、恢复

已知消息m和签名(r,s)，恢复计算出公钥Q。

(1)验证r, s∈n

(2)计算R=(x, y)，其中x=r,r+n,r+2n…，代入椭圆曲线方程计算获得R

(3)计算z = hash(m)

(4)计算u_1 = −zr^−1 mod n和u_2 = sr^−1 mod n

(5)计算公钥Q= (x’, y’)=u_1⋅G+u_2⋅R

#### 实验思路：
按照实现流程进行分部实现。

在进行验证算法之前，必须首先知道签发该交易所对应的公钥，因此需要在每笔交易中携带公钥，这需要消耗很大带宽和存储。故选择在生成的签名中携带recoveryID，之后进行公钥恢复。


#### 实验结果：

