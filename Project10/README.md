### 实验内容：
report on the application of this deduce technique in Ethereum with ECDSA
### 理论基础：
ECDSA 的安全性基于椭圆曲线离散对数问题，这是一种困难的数学问题，目前没有已知的高效算法可以在多项式时间内解决。因此，ECDSA 被认为是一种安全可靠的数字签名算法。ECDSA 的优点是具有较高的安全性、较小的密钥尺寸和快速的签名速度。缺点是需要选择合适的椭圆曲线和基点，并且在实现过程中需要注意安全性问题。

根据PPT讲述可以得到：

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project10/img/2.png)

可以概括为如下阶段：
#### ECDSA 的签名过程如下：

    (1)选择一个椭圆曲线和一个基点，这个基点必须是椭圆曲线上的一个点，并且不能是无穷远点。
    
    (2)随机生成一个私钥，私钥是一个随机数，通常使用伪随机数生成器生成。
    
    (3)使用私钥计算公钥，公钥是基点的一个倍数。
    
    (4)计算消息的哈希值。
    
    (5)使用私钥和哈希值生成签名，签名包括两个值：r 和 s。
    
    (6)将消息、签名和公钥一起发送给验证方。
#### ECDSA 的验证过程如下：

    (1)从签名中提取 r 和 s 值。
    
    (2)计算消息的哈希值。

    (3)使用公钥和哈希值验证签名是否正确。
### 实验思路：
由上述思路可以得到伪代码：
```python
# 生成公钥和私钥
private_key = generate_private_key()
public_key = get_public_key(private_key)

# 对消息进行签名
message = "0123456789"
signature = sign_message(message, private_key)

# 验证签名
is_valid = verify_signature(message, signature, public_key)
```
#### 在进行验证算法之前，必须首先知道签发该交易所对应的公钥，因此需要在每笔交易中携带公钥，这需要消耗很大带宽和存储。故选择在生成的签名中携带recoveryID，之后进行公钥恢复。
按照实现流程及伪代码进行实现。

### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project10/img/1.png)

