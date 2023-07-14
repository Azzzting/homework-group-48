#### 实验内容：
Schnorr Bacth
#### 理论基础：
Schnorr Batch是指Schnorr签名的批量处理技术。Schnorr签名是一种数字签名方案，其安全性基于离散对数问题。而Schnorr Batch的目标是提高批量生成和验证Schnorr签名的效率。

在传统的Schnorr签名方案中，每个签名需要独立进行计算和验证，这可能会导致高昂的计算开销，尤其是在需要处理大量签名的场景下。Schnorr Batch通过将多个签名的计算合并为一个集合，然后进行批量处理，从而减少了重复的计算步骤，提高了效率。

使用Schnorr Batch，可以将多个签名的计算和验证步骤合并为一个任务，以减少椭圆曲线运算和哈希计算等的开销。这种批量处理技术尤其在密码学协议和区块链系统中具有潜在的应用，因为它可以显著提高系统的性能和可扩展性。

总的来说，Schnorr Batch是一种利用批量处理技术提高Schnorr签名生成和验证效率的方法，适用于需要处理大量签名的场景，提供了更高的性能和可扩展性。
#### 实验思路：
1.生成私钥和公钥：

-对于每个签名参与者，生成一个随机的私钥。

-使用私钥和椭圆曲线上的基点，计算对应的公钥。

2.构建签名批次：

-确定需要生成或验证的签名数量。

-准备待签名的消息列表。

3.执行批量签名生成：

-为每个签名生成一个随机的值，称为r值。

-使用每个r值和椭圆曲线上的基点，计算承诺值（commitment）。

-对于每个消息，使用承诺值和消息进行哈希计算，生成摘要（digest）。

-使用摘要和私钥，计算签名中的s值。

-将承诺值和s值作为签名的结果。

4.执行批量签名验证：

-对于每个签名，获取承诺值、公钥和消息。

-使用承诺值和消息进行哈希计算，生成摘要。

-使用公钥、摘要和基点，验证签名的有效性。
#### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project21/img/1.png)