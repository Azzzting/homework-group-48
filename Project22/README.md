### 实验内容：
research report on MPT
### 理论基础：
Merkle Patricia Tree（MPT），也被称为Merkle Trie，是一种基于前缀树（Trie）的数据结构，用于高效地存储和验证加密货币领域中的关键数据，例如以太坊中的账户状态和交易历史。

MPT是对原始Patricia Trie的改进，由Ralph Merkle在1987年提出。其目标是提供一种紧凑、高效的方式来存储大量的键值对数据，并具备快速的查找、插入和删除操作。

#### MPT的核心思想是使用键的前缀作为树的节点，每个节点都包含一个键和相应的值。通过将键的字节序列拆分为不同的节点，可以有效地共享相同前缀的键，从而减少存储空间的需求。

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project22/img/1.png)

MPT的构建过程如下：

        (1)将要存储的键值对按照键进行排序。
        (2)逐个将键值对插入到MPT中。
        (4)如果当前节点不存在，则创建一个新的叶子节点，并将键值对存储在该节点中。
        (5)如果当前节点已经存在，则根据键的前缀继续延伸现有的节点。
        (6)对于非叶子节点，其值是一个哈希指针，指向下一个层级的节点。
        (7)在树的最底层，叶子节点存储实际的键值对数据。

由于MPT中的节点是通过哈希指针进行引用的，因此可以轻松地验证节点的完整性和完整树的一致性。通过比较节点的哈希值与存储在其他地方的根哈希值，可以验证整个树是否被篡改或损坏。在以太坊中，Merkle Patricia Tree被广泛用于存储和验证账户状态、交易历史和其他重要的区块链数据。它不仅提供了高效的存储和查找性能，而且具备了不可更改性和数据完整性的特性，有助于确保区块链的安全和一致性。
### 实验思路：
主要对构建MPT的关键步骤做了实现：

#### insert:

向MPT中插入一个键值对。它根据键逐层在MPT中找到合适的位置，并最终将值存储在叶子节点上。
```python
def insert(root, key, value):
    if not key:
        root.value = value
        return
    
    prefix = key[0]  # 当前键的前缀字符
    suffix = key[1:]  # 当前键的剩余字符
    
    if prefix not in root.children:
        root.children[prefix] = Node()
    
    insert(root.children[prefix], suffix, value)
```


#### construct_mpt：

用于构建完整的MPT,它接受一个键值对列表作为输入，并按照指定的块大小将数据分块处理。然后，调用build_block函数处理每个块的键值对数据，将其插入到MPT中。最后，返回构建好的MPT的根节点。
```python
def construct_mpt(key_value_pairs):
    root = Node()
    block_size = 100  # 每个块的大小
    
    for i in range(0, len(key_value_pairs), block_size):
        block_pairs = key_value_pairs[i:i+block_size]
        build_block(root, block_pairs)
    return root
```


#### build_block：

用于构建MPT的一个块，它接受一个块的键值对列表作为输入，并使用insert函数将每个键值对插入到MPT中。通过逐个处理块中的键值对，可以逐步构建较大的MPT。
```python
def build_block(root, block_pairs):
    for key, value in block_pairs:
        insert(root, key, value)
```
### 实验结果：
本实验完成了MPT构建简单构建：

测试信息：
```python

# 测试
mpt.insert('num1', '1')
mpt.insert('num2', '2')
mpt.insert('num3', '3')
mpt.insert('num4', '4')

print("key=num1 value=",mpt.get('num1')，1)  
print("key=num2 value=",mpt.get('num2')，2)  
print("key=num3 value=",mpt.get('num3')，3)
print("key=num4 value=",mpt.get('num4')，4)
```
由实验结果得：num1~num4均正确插入

![img](https://github.com/Azzzting/homework-group-48/blob/main/Project22/img/2.png)
