import base64
from gmssl import sm2, func
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT


print("------------------------sever加密--------------------------")
#生成SM2的密钥
sk_s = "00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5"
pk_s = "B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207"
sk_r = "228a9707053e1b333fb8cb839567a9db4ca1cf5381e9a6a539774e6c3563cdfa"
pk_r = "893cb9392dabd2fac095f657a7e0bc308e32f4b79380d478547f57123dccb3bc4a3a2d009f5826b6624c99dd41baf470a8baf46722f2d36b1d26f19af112c5cd"
print("Generate sm2Key......")
print("pk_s:",pk_s,"\npk_r:",pk_r)

# 创建sm4Key和sm4对象
print("\n协商会话密钥:")
sm4Key_str = func.random_hex(16)
sm4Key = bytes(sm4Key_str, encoding='utf-8') 
sm4_crypt = CryptSM4()
sm4_crypt.set_key(sm4Key, mode=SM4_ENCRYPT)
print("Session key：", sm4Key)

# 创建sm2对象,用pk_r对sm4Key进行加密
print("\n加密会话密钥：")
sm2_crypt = sm2.CryptSM2(private_key=None, public_key=pk_r) 
e_k = sm2_crypt.encrypt(sm4Key)  
e_k = base64.b64encode(e_k)
print("encryptKey",e_k)

# sm4对象对数据进行加密
print("\n加密信息：")
data ="1234567890"
data = data.encode("utf-8") 
e_data = sm4_crypt.crypt_ecb(data)
e_data = base64.b64encode(e_data)
e_data = e_data.decode("utf-8")
print("encryptData:",e_data)

# 用sk_s对sm4Key签名
print("\n使用私钥签名：")
sm2_crypt_s = sm2.CryptSM2(private_key=sk_s, public_key=None)
random_hex_str = func.random_hex(sm2_crypt.para_len)
sign = sm2_crypt_s.sign(sm4Key, random_hex_str)
sign = base64.b64encode(bytes(sign, encoding='utf-8'))
sign = sign.decode("utf-8")
print("sign:",sign)

print("\n发送(e_data||e_k||sign):")
result = {"encryptData":e_data,"e_k":e_k,"sign":sign}
print(result)


print("------------------------client解密--------------------------")
sign = base64.b64decode(result['sign'])
e_k =base64.b64decode(result["e_k"])
e_data = base64.b64decode(result["e_data"])

# sm2(附私钥)解密sm4Key
print("\n解出会话密钥：")
sm2_crypt_r =sm2.CryptSM2(private_key=sk_r,public_key=None)
sm4Key_r = sm2_crypt_r.decrypt(e_k)  # 解密, 返回bytes
print("Session Key that receiver obtain:",sm4Key_r)

# 公钥签名验证
print("\nVerify Sign with pk_s.....")
sm2_crypt_sr =sm2.CryptSM2(private_key=None,public_key=pk_s)
assert sm2_crypt_sr.verify(sign,sm4Key_r)

# sm4解密得到data
print("\n用公钥验证签名后解密信息：")
sm4_crypt_r=CryptSM4()
sm4_crypt_r.set_key(sm4Key_r,mode=SM4_DECRYPT)
data_r=sm4_crypt_r.crypt_ecb(e_data)
data_r = data_r.decode('utf-8')
print("data that receiver obtain:",data_r)
