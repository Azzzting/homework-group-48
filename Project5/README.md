### 实验内容：
Impl Merkle Tree following RFC6962
### 理论依据：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project5/img/3.png)


#### RFC6929:
RFC6962 是一份由谷歌公司发布的规范，描述了一种基于 Merkle Tree 的公共日志系统。该规范旨在提供一种可靠的方法来检测 SSL/TLS 证书的恶意或错误，并增强互联网的安全性。

RFC6962 规范定义了以下内容：

    (1)日志结构：描述了公共日志系统的结构和组成部分，包括日志服务器、客户端和 Merkle Tree。
    (2)日志操作：描述了向日志中添加新条目的过程，以及如何检索和验证这些条目。
    (3)Merkle Tree 的构建和验证：描述了如何使用哈希函数构建 Merkle Tree，并使用 Merkle Proof 验证数据块是否存在于 Merkle Tree 中。
    (4)安全性和隐私性：描述了如何保护日志系统的安全性和隐私性，包括如何防止攻击者篡改日志数据、如何保护用户隐私等。
#### Merkle trees:
Merkle trees的主要作用是快速归纳和校验区块数据的存在性和完整性。一般意义上来讲，它是哈希大量聚集数据“块”的一种方式，它依赖于将这些数据“块”分裂成较小单位的数据块，每一个bucket块仅包含几个数据“块”，然后取每个bucket单位数据块再次进行哈希，重复同样的过程，直至剩余的哈希总数仅变为1。

根据收集到的信息可以发现：

我们可以把Merkle Tree可以看做Hash List的泛化（Hash List可以看作一种特殊的Merkle Tree，即树高为2的多叉Merkle Tree）。

在最底层，和哈希列表一样，我们把数据分成小的数据块，有相应地哈希和它对应。但是往上走，并不是直接去运算根哈希，而是把相邻的两个哈希合并成一个字符串，然后运算这个字符串的哈希，这样每两个哈希可得到一个”子哈希“。如果最底层的哈希总数是单数，那到最后必然出现一个单哈希，这种情况就直接对它进行哈希运算，所以也能得到它的子哈希。于是往上推，依然是一样的方式，可以得到数目更少的新一级哈希，最终必然形成一棵倒挂的树，到了树根的这个位置，这一代就剩下一个根哈希了，我们把它叫做 Merkle Root。

Merkle tree和Hash list的主要区别是，可以直接下载并立即验证Merkle tree的一个分支。因为可以将文件切分成小的数据块，这样如果有一块数据损坏，仅仅重新下载这个数据块就行了。如果文件非常大，那么Merkle tree和Hash list都很到，但是Merkle tree可以一次下载一个分支，然后立即验证这个分支，如果分支验证通过，就可以下载数据了。而Hash list只有下载整个hash list才能验证。
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project5/img/2.png)

#### 关键步骤的伪代码实现(仅示例)：
Merkle Proof 是一种证明，用于证明某个数据块存在于 Merkle Tree 中。它包括从该数据块到根节点的路径上的所有哈希值，以及另一些已知的哈希值。
##### 构建Merkle tree
```python
def build_tree(self, data):
        nodes = [Node(value=hash(value)) for value in data]
        while len(nodes) > 1:
            parent_nodes = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i+1] if i+1 < len(nodes) else left
                parent_nodes.append(Node(value=hash(left.value+right.value), left=left,right=right))
            nodes = parent_nodes
        return nodes[0]
```
##### 获取 Merkle Proof
```python
 def get_proof(self, value):
        node = self.get_node(value)
        proof = []
        while node != self.root:
            if node == node.parent.left:
                proof.append(node.parent.right.value)
            else:
                proof.append(node.parent.left.value)
            node = node.parent
        return proof
```
##### 验证 Merkle Proof
```python
def validate_proof(self, value, proof):
        node = Node(value=hash(value))
        for p in proof:
            if node == node.parent.left:
                node = Node(value=hash(node.value+p))
            else:
                node = Node(value=hash(p+node.value))
        return node.value == self.root.value
```
##### 获取节点
```python
def get_node(self, value):
        for node in self.traverse():
            if node.value == hash(value):
                return node
```
##### 遍历
```python
def search(self):
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            if node.left:
                node.left.parent = node
                nodes.append(node.left)
            if node.right:
                node.right.parent = node
                nodes.append(node.right)
            yield node
```
### 实验思路：
依照理论依据所描述可以分为以下几个步骤：

    (1)在最底层，和哈希列表一样，可以把数据分成小的数据块，有相应地哈希和它对应。 
    (2)当从叶子节点向上计算时，将相邻的两个哈希合并，然后运算这个新值的哈希，这样每两个哈希形成一个"子哈希"。 
    (3)如果最底层的哈希总数是单数，那到最后必然出现一个哈希无法和其他哈希进行合并，此时直接对它进行哈希运算得到它的子哈希。 
    (4)如此循环向上进行合并，可以得到数目更少的新一级哈希，最终必然形成一棵倒挂的树，到了根节点的位置时，只剩下一个跟哈希了。
    (5)依据伪代码实现完成详细代码实现。

    
#### 实验结果：
![img](https://github.com/Azzzting/homework-group-48/blob/main/Project5/img/1.png)
