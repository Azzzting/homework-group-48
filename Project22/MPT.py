import hashlib

class MerklePatriciaTree:
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

# 测试样例：
tree = MerklePatriciaTree()
tree.insert('key1', 'value1')
tree.insert('key2', 'value2')
tree.insert('key3', 'value3')

print(tree.get('key1'))  # 输出：value1
print(tree.get('key2'))  # 输出：value2
print(tree.get('key3'))  # 输出：value3
print(tree.get('key4'))  # 输出：None
