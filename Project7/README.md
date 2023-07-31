### 实验内容：
Try to Implement this scheme
### 理论基础：
HashWires: Hyperefficient Credential-Based Range Proofs

HashWires 是一种基于区块链的去中心化数据存储系统，其中包含了一种称为 Hyperefficient Credential-Based Range Proofs（具有超高效证书的区间证明）的证明机制。该机制可以同时提高证明的大小和生成效率。

具体来说，HashWires 的 Hyperefficient Credential-Based Range Proofs 机制采用了一种新型的哈希链结构，称为 HashWire。HashWire 可以将多个证书压缩成一个证书，并将证书的大小从 O(n) 压缩到 O(log n)。这是通过在每个证书上附加一个哈希值并将其链接到前一个证书来实现的。因此，HashWire 本质上是一种哈希链，其中每个哈希值都对应于一个证书。

使用 HashWire，Hyperefficient Credential-Based Range Proofs 可以在 O(log n) 的时间内生成，并且证明的大小也只有 O(log n)。这比传统的区间证明机制要快得多，并且可以节省大量空间，使其在去中心化数据存储系统中更加实用。

总之，HashWires 的 Hyperefficient Credential-Based Range Proofs 机制通过引入 HashWire 哈希链结构，将证书压缩到 O(log n) 的大小，并在 O(log n) 的时间内生成区间证明，从而提高了证明的大小和生成效率。

hashwire官方文档:https://zkproof.org/2021/05/05/hashwires-range-proofs-from-hash-functions/
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project7/img/1.png)
### 实验思路：
#### 关键部分的伪代码实现：
##### 计算区块的哈希值
```python
def calculate_hash(self):
        sha = hashlib.sha256()
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        sha.update(block_string)
        return sha.hexdigest()
```
##### 创建创世区块
```python
    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")
```
##### 添加新区块
```python
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
```
##### 验证区块链是否有效
```python
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
```
根据PPT流程介绍、文档内容及网络搜索结果，可以对其进行简单实现：

    (1)定义了 HashWire 类，该类用于创建哈希链，并提供添加证书和获取根哈希值的方法。

    (2)定义了 RangeProof 类，该类用于生成区间证明。

    (3)在 RangeProof 类的构造函数中，将输入的值列表转换为字符串，并将每个字符串添加到哈希链中。
    
    (4)在 generate_proof() 方法中，首先检查给定的起始索引和结束索引是否在列表的有效范围内。如果不是，则返回 None。如果是，则遍历哈希链，直到到达结束索引或哈希链的末尾为止。

    (5)在遍历哈希链时，只添加给定区间内的节点的证书到证明中。如果当前节点没有后继节点，则已经到达了哈希链的末尾，因此停止遍历。
    
    (6)最后，返回生成的区间证明。
### 实验结果：
    
    测试数据为：values = [1, 2, 3, 4, 5]
    range_proof = RangeProof(values)
    proof = range_proof.generate_proof(1, 3)
    也就是说我们从索引1（即第二个元素）开始，到索引3（即第四个元素）结束，因此我们期望得到的区间证明将包含值 2, 3, 和 4。
    代码返回值是其sha().hexdigest()
    进行验证：符合要求返回2，3，4
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project7/img/2.png)
### 实验不足：
由于理论较高深，自身水平有限，未能完整实现文档中提及的功能。会在后续的学习中继续努力。
