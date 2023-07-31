#### 实验内容：
implement the Rho method of reduced SM3
#### 理论基础：
思路等同于在密码学引论中涉及到因子分解时用到的Pollard Rho:根据一个初始的值，不断进行哈希，最终形成回路。

因子分解用到的Rho:

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project2/img/1.png)

本实验所用到的Rho:

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project2/img/2.png)

伪代码实现：
```python
Function PollardRho(n):
    x ← 2
    y ← 2
    d ← 1
    
    Function f(x):
        return (x^2 + 1) % n
    
    While d == 1:
        x ← f(x)
        y ← f(f(y))
        d ← gcd(|x - y|, n)
    
    If d == n:
        Return "Failure"
    Else:
        Return d

```

#### 实验思路：
根据伪代码可知具体步骤如下：

    (1) 首先，选择一个起始点x和一个用于计算下一个序列项的函数f(x)。通常选择f(x) = (x^2 + 1) % n，其中%表示取模运算。初始化y和d，其中y是通过f(x)计算出来的第二个序列项，d是一个辗转相除法（gcd）的中间结果，默认将d设置为1。
    
    (2) 在一个循环中，重复执行以下步骤，直到找到非平凡因子（即d != 1）或者算法失败（d == n）：
            --更新x为f(x)的结果。
            --更新y为f(f(y))的结果，即连续两次应用f函数。
            --计算|x - y|的绝对值，并利用gcd函数求得|x - y|与n的最大公约数。
            --如果最大公约数d等于n，表示算法失败，无法找到非平凡因子。
            --在循环结束后，根据d的值判断算法的结果。

    (3) 如果d等于n，表示算法失败，无法找到非平凡因子。否则，d是n的一个非平凡因子。

在具体实现中：考虑使用快速幂算法计算幂，使用Miller-Rabin素性检测来判断质因数的存在性等。


#### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project2/img/3.png)

#### 实验不足：
通过对实验数据的测试发现，随着bit数不断增长，所消耗时间激增。

可能的原因是代码中采用循环结构，当构造的消息长度较长时，程序运行时间受到明显影响。

在后续的实现中可以采用多线程、循环展开、流水线等可能改进的措施进行尝试与改进。
