### 实验内容：
impl this protocol with actual network communication
### 理论基础：
Range Proof是一种协议或机制，用于证明某个数值或数值范围的真实性，而不必直接披露该数值的具体值。

关键步骤的伪代码实现：
#### Alice 生成证明
```python
def alice_generate_proof(min_val, max_val, value, r):
    # 计算 A 和 S 值
    A = g ** r
    S = (value - min_val) * h ** r
    # 发送 A 和 S 值给 Bob
    send(A, S)
    # 接收挑战值 e
    e = receive()
    # 计算 z 值
    z = r + e * (max_val - min_val)
    # 发送 z 值给 Bob
    send(z)
```
#### Bob 验证证明
```python
def verify_proof(min_val, max_val):
    # 接收 A 和 S 值
    A = receive()
    S = receive()
    # 生成挑战值 e
    e = random()
    # 发送挑战值 e 给 Alice
    send(e)
    # 接收 z 值
    z = receive()
    # 验证证明是否有效
    if A == g ** z * h ** (-e * min_val) and S == (g ** (-e) * h) ** (z - min_val):
        return True
    else:
        return False
```
#### Alice 和 Bob 进行通信
```python
if __name__ == '__main__':
    min_val = 10
    max_val = 1000
    value = 500
    r = random()

    generate_proof(min_val, max_val, value, r)
    result = verify_proof(min_val, max_val)

    if result:
        print("Range proof is valid")
    else:
        print("Range proof is invalid")

```


### 实验思路：
在这个具体的示例中，Range Proof用于证明Alice的年龄大于21岁，而不需要直接透露她的具体年龄。

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project6/img/3.png)

依据理论基础及PT中的流程图可以得到：

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project6/img/4.png)

    (1)Trusted Issuer选择一个128位的随机种子，并使用哈希函数计算H0(seed)得到初始哈希值h0。
    
    (2)计算k = 当前年份 - 出生年份，然后将h0和k作为输入，使用哈希函数计算H1(h0, k)得到哈希值c。这个哈希值c将用作主要证明的依据。
    
    (3)信任颁发者将计算得到的种子s和c的签名sigc传递给Alice。
    
    (4)Alice为了向Bob证明自己的年龄大于21岁，计算d0 = 21 - 出生年份，并使用s作为种子，使用哈希函数计算H1(d0, s)得到证明的哈希值p。
    
    (5)Alice将证明的哈希值p和c的签名传递给Bob。
    
    (6)Bob接收到Alice传递的信息后，根据当前年份和d0计算d1 = 当前年份 + d0，并使用哈希函数计算H1(d1, p)得到哈希值c1。然后，Bob验证c与c1是否一致，以确认签名sigc是用来验证c1的。
    
    (7)如果验证通过，Bob确认Alice的年龄大于21岁；否则，认为验证失败。

  
### 实验结果：
#### proof_Hash_Function.py函数是对协议的具体实现，可以进行无网络的验证。

#### test.py函数是加上网络通信之后的实现。
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project6/img/2.png)
