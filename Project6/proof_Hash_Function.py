from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15

def prove_age(seed, birth_year, current_year):
    # H0(seed)
    h0 = SHA256.new(seed.encode()).digest()

    # k and c
    k = current_year - birth_year
    h1 = SHA256.new()
    h1.update(h0)
    h1.update(str(k).encode())
    c = h1.digest()

    # Alice的公私钥
    alice_key = RSA.generate(2048)
    alice_private_key = alice_key.export_key()
    alice_public_key = alice_key.publickey().export_key()

    alice_signature_key = RSA.import_key(alice_private_key)

    # d0, proof, and signature
    d0 = 21 - birth_year
    h1_d0 = SHA256.new()
    h1_d0.update(h0)
    h1_d0.update(str(d0).encode())
    proof = h1_d0.digest()

    # Alice使用公钥签名
    signature = pkcs1_15.new(alice_signature_key).sign(proof)

    # Bob验证
    h1_d1 = SHA256.new()
    h1_d1.update(h1.digest())
    d1 = current_year + d0
    h1_d1.update(str(d1).encode())
    c1 = h1_d1.digest()

    # 用公钥验证
    alice_verification_key = RSA.import_key(alice_public_key)
    verifier = pkcs1_15.new(alice_verification_key)

    try:
        verifier.verify(proof, signature)
        return "Bob: Proof verified. Alice's age is greater than 21."
    except (ValueError, TypeError):
        return "Bob: Proof verification failed. Alice's age is not greater than 21."

# 测试案例
seed = "random_seed"
birth_year = 1978
current_year = 2021

result = prove_age(seed, birth_year, current_year)
print(result)
