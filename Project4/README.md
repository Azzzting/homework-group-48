#### 实验内容：
do your best to optimize SM3 implementation (software)
#### 理论基础：
一般对于程序性能的优化，可以采取以下几种常见方式：减少循环结构，对其进行循环展开等操作；利用存储结构的局部性，时间局部性和空间局部性，减少对数组的存取操作等；利用并行性，SIMD、数据流等方法。

对于具体的SM3算法，可以通过分析其算法结构，有针对性的进行优化：消息扩展部分、压缩函数部分等关键部件。
#### 实验思路：
本次实验采取对已有的SM3算法进行优化，通过对同样数据量的时间消耗测量显示优化结果。

##### 优化点1：利用局部性，减少对数组元素的访问，减少运行时间。

原代码：
```c
for (int i = 0; i < str.size(); i++)

{

	if (str[i] >= 'A' && str[i] <= 'F')

		bin += table[str[i] - 'A' + 10];

	else

		bin += table[str[i] - '0'];

}
```
修改：

可将其中对数组访问的语句str[i]都改为char temp = str[i] 后使用temp访问。
##### 优化点2：使用循环展开，利用局部性，同时访问多个变量，提升运行速度。
原代码：
```c
for (int i = 0; i < str.size(); i++)

{

	if (str[i] >= 'A' && str[i] <= 'F')

		bin += table[str[i] - 'A' + 10];

	else

		bin += table[str[i] - '0'];

}
```
修改：

可将其变为
```c
char temp1 = str[i];
char temp2 = str[i + 1];
```
##### 优化点3：采用多线程编程SIMD
单独对

#### 实验结果：
