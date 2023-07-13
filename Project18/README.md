#### 实验内容：
send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself
#### 理论基础：
数据信息均来自于Bitcon测试网站：https://blockstream.info/testnet/

如图所示是一笔交易信息：

Hash:是这个区块的前一个区块的hash值。也就是矿工要进行计算的值。

Status:Confirmation Time：交易确认时间是指一个交易从被提交到获得足够多的确认所需的时间。在比特币网络中，确认时间取决于网络拥堵程度和交易费用。在网络不拥堵的情况下，交易通常可以在几分钟内获得首次确认，对于更多的确认通常需要更长的时间。

TimeStamp:时间戳用来标识这个区块挖出的时间。

Height:指的是这个区块之前区块的数量。

Size:交易的大小。

Virtual Size:虚拟大小。

Wight Units:权重单位，是用于计量交易和区块的指标。

Number of transaction：这个区块内部交易的数量。
#### 实验思路：
选用一个测试案例来实现整个签名流程及对结果的解析：

1.生成新的私钥和地址

2.向生成的地址请求0.01个测试网币

3.创建交易并添加输入和输出

4.使用私钥对交易进行签名

5.打印原始交易数据

6.反序列化原始交易数据并打印解析结果
#### 实验结果：
