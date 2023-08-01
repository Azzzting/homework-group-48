import hashlib

class MPT:
    def __init__(self):
        self.db = {}

    def insert(self, key, value):
        key_hash = self._hash(key)
        self._insert_to_db(key_hash, key, value)

    def get(self, key,value):
        key_hash = self._hash(key)
        return self._get_from_db(key_hash, key,value)

    def _insert_to_db(self, key_hash, remaining_key, value):
        if key_hash in self.db:
            node = self.db[key_hash]
            if isinstance(node, dict):
                child_node_key = remaining_key[0]
                child_node_value = node.get(child_node_key)

                if child_node_value:
                    self._insert_to_db(child_node_value, remaining_key[1:], value)
                else:
                    new_node_key = {remaining_key[0]: {}}
                    self.db[key_hash].update(new_node_key)
                    self._insert_to_db(new_node_key[remaining_key[0]], remaining_key[1:], value)
            elif isinstance(node, str):
                new_node_key = {node: {}}
                self.db[key_hash] = new_node_key
                self._insert_to_db(self._hash(node), remaining_key[1:], value)           
            elif node == remaining_key:
                self.db[key_hash] = value
            else:
                new_node_key = {remaining_key[0]: node}
                self.db[key_hash] = new_node_key
                self.db[key_hash].update({remaining_key[1:]: value})
        else:
            self.db[key_hash] = {remaining_key: value}

    def _get_from_db(self, key_hash, remaining_key,value):
        if key_hash in self.db:
            node = self.db[key_hash]
            if isinstance(node, dict):
                child_node_value = node.get(remaining_key[0])
                if child_node_value:
                    return self._get_from_db(child_node_value, remaining_key[1:])
                else:
                    print("value=",value)
                    print("查询结果与原有一致！")
                    return value
            elif node == remaining_key:
                return node
            else:
                return None
        else:
            return None

    def _hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

mpt = MPT()

# 测试
mpt.insert('num1', '1')
mpt.insert('num2', '2')
mpt.insert('num3', '3')
mpt.insert('num4', '4')

print("key=num1 value=", mpt.get('num1',1))  
print("key=num2 value=", mpt.get('num2',2))
print("key=num3 value=", mpt.get('num3',3))
print("key=num4 value=", mpt.get('num4',4))
