### 实验内容：
forge a signature to pretend that you are Satoshi
### 理论基础：
#### 中本聪创世区块挖矿地址1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa；

转成ASCII码十六进制为3141317a5031655035514765666932444d505466544c35534c6d7637446976664e61；

PPT中得到伪造私钥的步骤如下：

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project19/img/2.png)

完整步骤如下：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project19/img/3.png)
### 实验思路：
对于使用ECDSA签名，在前几个Project中已有详述，故不在赘述。

本实验为了证明是中本聪，则需要对创世区块挖矿的地址+原消息+签名”进行验证。

即需要知道中本聪的公钥，签名和计算的hash。

在网上搜索到如下：

    P=[26877259512020005462763638353364532382639391845761963173968516804546337027093, 48566944205781153898153509065115980357578581414964392335433501542694784316391] 
    r,s=41159732757593917641705955129814776632782548295209210156195240041086117167123, 57859546964026281203981084782644312411948733933855404654835874846733002636486
### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project19/img/1.png)
