import hashlib
import json

class HashWire:
    def __init__(self):
        self.head = None

    # 添加证书
    def add_certificate(self, certificate):
        if self.head is None:
            self.head = {
                "certificate": certificate,
                "hash": None
            }
        else:
            new_node = {
                "certificate": certificate,
                "hash": None
            }
            new_node["hash"] = self._calculate_hash(new_node["certificate"], self.head["hash"])
            self.head = new_node

    # 获取 HashWire 的根哈希值
    def get_root_hash(self):
        if self.head is None:
            return None
        return self.head["hash"]

    # 计算哈希值
    def _calculate_hash(self, certificate, previous_hash):
        sha = hashlib.sha256()
        if previous_hash is not None:
            data = certificate.encode() + previous_hash.encode()
        else:
            data = certificate.encode()
        sha.update(data)
        return sha.hexdigest()

class RangeProof:
    def __init__(self, values):
        self.values = values
        self.hash_wire = HashWire()
        for value in values:
            self.hash_wire.add_certificate(str(value))

    # 生成区间证明
    def generate_proof(self, start_index, end_index):
        if start_index < 0 or end_index >= len(self.values):
            return None
        if start_index > end_index:
            return None

        proof = []
        current_node = self.hash_wire.head
        for i in range(len(self.values)):
            if i >= start_index and i <= end_index:
                proof.append(current_node["certificate"])
            if current_node["hash"] is None:
                break
            current_node = {
                "certificate": current_node["hash"],
                "hash": None
            }
            current_node["hash"] = self.hash_wire._calculate_hash(current_node["certificate"], current_node["hash"])
            print(current_node)
        return proof

# 测试代码
values = [1, 2, 3, 4, 5]
range_proof = RangeProof(values)
a,b=1,3
c=[]
proof = range_proof.generate_proof(a, b)
print("final result:")
print(proof)
for i in range(a,b+1):
    c.append(values[i])
print(c)
