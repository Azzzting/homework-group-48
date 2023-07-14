import hashlib

class MPT:
    def __init__(self):
        self.db = {}  # 使用字典作为存储数据库

    def insert(self, key, value):
        key_hash = self._hash(key)
        self._insert_to_db(key_hash, key, value)

    def get(self, key):
        key_hash = self._hash(key)
        return self._get_from_db(key_hash, key)

    def _insert_to_db(self, key_hash, remaining_key, value):
        if key_hash in self.db:
            node = self.db[key_hash]
            if isinstance(node, dict):  # 包含子节点的情况
                self._insert_to_db(node[remaining_key[0]], remaining_key[1:], value)
            else:  # 叶节点的情况
                new_node = {remaining_key[0]: node, remaining_key[1:]: value}
                self.db[key_hash] = new_node
        else:
            self.db[key_hash] = {remaining_key: value}

    def _get_from_db(self, key_hash, remaining_key):
        if key_hash in self.db:
            node = self.db[key_hash]
            if isinstance(node, dict):  # 包含子节点的情况
                return self._get_from_db(node[remaining_key[0]], remaining_key[1:])
            elif node == remaining_key:
                return node
            else:  # 叶节点的情况
                return None
        else:
            return None

    def _hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()  # 假设使用SHA256哈希函数
mpt=MPT

# 测试
mpt.insert('num1', '1')
mpt.insert('num2', '2')
mpt.insert('num3', '3')
mpt.insert('num4', '4')

print("key=num1 value=",mpt.search('num1'))  
print("key=num2 value=",mpt.search('num2'))  
print("key=num3 value=",mpt.search('num3'))
print("key=num4 value=",mpt.search('num4'))
print("key=num5 value=",mpt.search('num5'))
