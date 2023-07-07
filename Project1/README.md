#### 实验内容：
implement the naïve birthday attack of reduced SM3
#### 理论基础：
生日攻击利用生日悖论，当明文长度为n时，找到与其相同输出的消息的复杂度为O(2^n/2)；且构造出有效消息时容易的。
#### 实验思路：
本实验采取在消息空间中随机构造明文并对其进行加密，将加密结果与之前存入的结果进行对比：对比不成功则加入；对比成功时，说明找到了碰撞。
#### 实验结果
首先尝试对25bit、30bit进行碰撞：

![image](https://github.com/Azzzting/homework-group-48/blob/main/Project1/img/1.png)


之后对32bit进行实验时发现，其所消耗时间激增：

![image](https://github.com/Azzzting/homework-group-48/blob/main/Project1/img/2.png)


最终尝试结果为：本算法可以对前40bit进行碰撞：

![image](https://github.com/Azzzting/homework-group-48/blob/main/Project1/img/3.png)
