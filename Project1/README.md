#### 实验内容：
implement the naïve birthday attack of reduced SM3
#### 理论基础：
总述：

(1)生日攻击利用生日悖论，当明文长度为n时，找到与其相同输出的消息的复杂度为O(2^n/2)

(2)构造出有效消息是容易的

##### 生日攻击及复杂度推导：

生日问题也叫做生日悖论，它是这样这样描述的。

假如随机选择n个人，那么这个n个人中有两个人的生日相同的概率是多少。如果要想概率是100%，那么只需要选择367个人就够了。因为只有366个生日日期（包括2月29日）。

如果想要概率达到99.9% ，那么只需要70个人就够了。50%的概率只需要23个人。

##### 概率分布图如下所示：

![image](https://github.com/Azzzting/homework-group-48/blob/main/Project1/img/4.png)

根据上述描述我们可以得到如下公式，达到50%成功率的需要：

![image](https://github.com/Azzzting/homework-group-48/assets/138744150/669d00e2-d96f-4535-88e4-725e2612e85f)

##### 即得到了复杂度近似为O(2^n/2)


#### 实验思路：
本实验采取在消息空间中随机构造明文并对其进行加密，将加密结果与之前存入的结果进行对比：对比不成功则加入；对比成功时，说明找到了碰撞。
#### 实验结果
首先尝试对25bit、30bit进行碰撞：

![image](https://github.com/Azzzting/homework-group-48/blob/main/Project1/img/1.png)


之后对32bit进行实验时发现，其所消耗时间激增：

![image](https://github.com/Azzzting/homework-group-48/blob/main/Project1/img/2.png)


最终尝试结果为：本算法可以对前40bit进行碰撞：

![image](https://github.com/Azzzting/homework-group-48/blob/main/Project1/img/3.png)
