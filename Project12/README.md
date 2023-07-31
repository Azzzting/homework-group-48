### 实验内容：
verify the above pitfalls with proof-of-concept code
### 理论基础：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project12/img/2.png)
#### Leaking k leads to leaking of d:
$s=k^{-1}(e+dr)\pmod{n}$，可推得 $d=(sk-e)r^{-1}\pmod{n}$，若已知 $k$，则可以直接得到 $d$。
#### Reusing k leads to leaking of d:
    若两次签名使用同一个k，那么有 r = r_1 = r_2 s_1=k^{-1}(e_1+dr) s_2=k^{-1}(e_2+dr)
    即 ks_1=(e_1+dr) ks_2=(e_2+dr)，两式相除可得 s_1/s_2=(e_1+dr)/(e_2+dr)
    整理可得 s_1e_2/s_2 +s_1dr/s_2=e_1+dr d=(e_1-s_1e_2/s_2)/(s_1r/s_2-r) d=(e_1s_2-s_1e_2)/(s_1r-rs_2)
#### Two users, using k leads to leaking of d, that is they can deduce each other’s d:
    若两个用户使用同样的k加密签名，那么有 r=r_1=r_2 s_1k=(e_1+d_1r) s_2k=(e_2+d_1r)
    第一个式子乘 s_2，第二个式子乘 s_1，可以得到 s_1s_2k=(s_2e_1+s_2rd_1) s_1s_2k=(s_1e_2+s_1rd_1)
    那么有 s_2rd_1=s_1e_2+s_1rd_2-s_2e_1，由此方程可求得 d_1。
#### Malleability of ECDSA, e.g. $(r,s)$ and $(r,-s)$ are both valid signatures, lead to blockchain network split:
    对于 (r,s) 验签，计算 es^{-1}G+rs^{-1}P=(x',y')
    若 r=x' 则通过验证；对于 (r,-s)，计算 e(-s)^{-1}G+r(-s)^{-1}P=-(es^{-1}G+rs^{-1}P)=(x',-y')
    得到的点的横坐标同样是 x'，可通过验证。
### 实验思路：
根据理论依据编写代码：
#### 针对情况1：
```python
def know_k(k, G, P, n, e, r, s):
    d = ((s * k - e) * inverse(r, n)) % n
    return d
```
#### 针对情况2：
```python
def reknow_k(k1, k2, G, P, n, e1, e2, r1, s1, r2, s2):
    r = r1
    d = ((e1 * s2 - s1 * e2) * inverse(s1 * r - r * s2, n)) % n
    return d
```
#### 针对情况3：
```python
def same_k(k, G, P, n, d2, e1, e2, r1, s1, r2, s2):
    r = r1
    d1 = (inverse(s2 * r, n) * (s1 * e2 - s2 * e1 + s1 * r * d2)) % n
    return d1
```
#### 针对情况4：
```python
def Verify(P, e, n, G, r, s): 
    w = inverse(s, n) % n
    t1 = (e * w) % n
    t2 = (r * w) % n
    X = add(mult(t1, G), mult(t2, P))
    if X == None:
        print("the sig invalid")
        return
    else:
        r_ = X[0] % n
    if r == r_:
        return 1
    else:
        return 0
```
### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project12/img/3.png)
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project12/img/4.png)
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project12/img/5.png)
### 实验思考:
在实现的过程中感觉到它存在的种种问题在RSA签名时也存在，感觉这是公钥签名体系的一些通病。

RSA为了抵抗这些缺陷采取了RSA-OAEP的安全版本，那么这几种方式是不是也有对应的措施？是否也为了安全引用了HASH函数？

希望能在之后的学习中找到答案。
