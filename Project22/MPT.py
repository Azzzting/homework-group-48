import hashlib

class MPT:
    def __init__(self):
        self.db = {}

    def insert(self, key, value):
        key_hash = self._hash(key)
        self._insert_to_db(key_hash, key, value)

    def get(self, key):
        key_hash = self._hash(key)
        return self._get_from_db(key_hash, key)

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
                    self._insert_to_db(child_node_value, remaining_key[1:], value)
                        
            elif node == remaining_key:
                self.db[key_hash] = value
            else:
                new_node_key = {remaining_key[0]: node}
                self.db[key_hash] = new_node_key
                self.db[key_hash].update({remaining_key[1:]: value})
        else:
            self.db[key_hash] = {remaining_key: value}

    def _get_from_db(self, key_hash, remaining_key):
        if key_hash in self.db:
            node = self.db[key_hash]
            if isinstance(node, dict):
                child_node_value = node.get(remaining_key[0])
                if child_node_value:
                    return self._get_from_db(child_node_value, remaining_key[1:])
                else:
                    return None
            elif node == remaining_key:
                return node
            else:
                return None
        else:
            return None

    def _hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()
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
