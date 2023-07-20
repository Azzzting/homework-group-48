from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
import socket

def prove_age(seed, birth_year, current_year):
    h0 = SHA256.new(seed.encode()).digest()
    k = current_year - birth_year
    h1 = SHA256.new()
    h1.update(h0)
    h1.update(str(k).encode())
    c = h1.digest()
    alice_key = RSA.generate(2048)
    alice_private_key = alice_key.export_key()
    alice_public_key = alice_key.publickey().export_key()
    alice_signature_key = RSA.import_key(alice_private_key)
    d0 = 21 - birth_year
    h1_d0 = SHA256.new()
    h1_d0.update(h0)
    h1_d0.update(str(d0).encode())
    proof = h1_d0.digest()
    signature = pkcs1_15.new(alice_signature_key).sign(proof)
    h1_d1 = SHA256.new()
    h1_d1.update(h1.digest())
    d1 = current_year + d0
    h1_d1.update(str(d1).encode())
    c1 = h1_d1.digest()
    alice_verification_key = RSA.import_key(alice_public_key)
    verifier = pkcs1_15.new(alice_verification_key)

    try:
        verifier.verify(proof, signature)
        return "Bob: Proof verified. Alice's age is greater than 21."
    except (ValueError, TypeError):
        return "Bob: Proof verification failed. Alice's age is not greater than 21."


#服务器端：
# 定义主机和端口
host = '127.0.0.1'
port = 50007

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定主机和端口
server_socket.bind((host, port))

# 开始监听
server_socket.listen(1)
print('Waiting for a connection...')

while True:
    # 等待客户端连接
    client_socket, client_address = server_socket.accept()
    print('Connected from:', client_address)

    # 接收客户端发送的数据
    data = client_socket.recv(1024).decode()
    seed, birth_year, current_year = data.split(',')

    # 处理数据并生成验证结果
    result = prove_age(seed, int(birth_year), int(current_year))
    
    # 发送验证结果给客户端
    client_socket.send(result.encode())

    # 关闭客户端连接
    client_socket.close()


#客户端：
# 定义服务器的主机和端口
host = '127.0.0.1'
port = 50007

# 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect((host, port))

# 准备要发送的数据
seed = "random_seed"
birth_year = str(1978)
current_year = str(2021)
data = seed + ',' + birth_year + ',' + current_year

# 发送数据给服务器
client_socket.send(data.encode())

# 接收服务器返回的验证结果
result = client_socket.recv(1024).decode()
print(result)

# 关闭连接
client_socket.close()
