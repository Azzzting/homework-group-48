import bitcoinlib

bitcoinlib.SelectParams("https://blockstream.info/testnet/")
private_key = bitcoinlib.keys.PrivateKey()
address = private_key.public_key.address()

# 创建交易
tx = bitcoinlib.Transaction()
tx.inputs.append(bitcoinlib.Input(address, 0))
output_address = "tb1qjctmj82x6phc8x9y2cd3hrgy4zyl3n0qjqplc8"
output_value = 0.005
tx.outputs.append(bitcoinlib.TxOutput(output_address, output_value))
tx.sign(private_key)

# 打印原始交易数据
raw_tx = tx.serialize()
print("原始交易数据：", raw_tx)

# 解析交易数据
parsed_tx = bitcoinlib.Transaction.deserialize(raw_tx)
print("解析结果：", parsed_tx)
