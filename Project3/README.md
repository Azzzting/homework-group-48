#### 实验内容：
implement length extension attack for SM3, SHA256, etc.
#### 理论基础：
当MD结构使用MD强化模式时，可以对其进行长度扩展攻击。

![images](https://github.com/Azzzting/homework-group-48/blob/main/Project3/img/2.png)

即在敌手不知道M1具体信息但知道信息M1的hash值，在M1之后级联上M2=00... ...0|| |M1|，得到新的hash值，此时即完成扩展长度攻击。

#### 实验思路：
首先需要对明文进行填充，随后对其进行分组并加密。

之后计算原M1的hsah值和扩展之后的hash值

最后对其判断是否相等：相等则证明攻击成功。
#### 实验结果：
![images](https://github.com/Azzzting/homework-group-48/blob/main/Project3/img/1.png)
#### 实验心得：
原本库中的SM3在实施扩展时具有一些缺陷，可以在后续实验中对其进行更改。

由于长度扩展攻击是针对MD的结构性攻击，是难以从理论上的抵抗，但其应用广泛。可以在后续的学习中，对其进行深入学习。
