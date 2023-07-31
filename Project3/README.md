### 实验内容：
implement length extension attack for SM3, SHA256, etc.
### 理论基础：
#### 当MD结构使用MD强化模式时，可以对其进行长度扩展攻击。

![images](https://github.com/Azzzting/homework-group-48/blob/main/Project3/img/2.png)

即在敌手不知道M1具体信息但知道信息M1的hash值，在M1之后级联上M2=00... ...0|| |M1|，得到新的hash值，此时即完成扩展长度攻击。

伪代码实现：
```python

original_message = "yuanshi"
original_hash = "xxxx" 

extra_data = "tianjia"
constructed_hash = original_hash + extra_data
constructed_message_length = len(original_message) + len(extra_data)
new_hash = hashlib.sha256(constructed_hash).hexdigest()
```

### 实验思路：
根据伪代码可以得到实验思路：

        (1) 原始消息和已知长度的哈希值

        (2) 预先计算哈希值的中间状态及其长度

        (3) 需要构造的输入：原始消息 + 后续数据 + 填充

        (4)计算填充字节的数量并构建填充字节:  padding_bytes = (-(len(constructed_input) + state_length + 1)) % state_length
        
        (5) 构造伪造消息及填充长度: new_message = constructed_input + padding + suffix_data
                                  new_length = (len(constructed_input) + len(padding) + len(suffix_data)) * 8
        
        (6) 计算伪造哈希摘要
### 实验结果：
![images](https://github.com/Azzzting/homework-group-48/blob/main/Project3/img/1.png)
### 实验心得：
原本库中的SM3在实施扩展时具有一些缺陷，将在后续实验中对其进行更改。

由于长度扩展攻击是针对MD的结构性攻击，是难以从理论上的抵抗，但却应用广泛，那么一定有过人之处。将在后续的学习中，对其进行深入学习。
